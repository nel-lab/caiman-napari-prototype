"""Create simple callback that modifies the line visual."""
from skimage import data
from skimage import measure
import numpy as np
import napari
from napari import Viewer
from napari.layers import Shapes
import napari_plot
from napari_plot._qt.qt_viewer import QtViewer
from qtpy.QtWidgets import QVBoxLayout
from caiman import load_memmap
from mesmerize_napari.utils import *
import caiman as cm
import pandas as pd
import pyqtgraph as pg
from napari._qt.widgets.qt_viewer_dock_widget import QtViewerDockWidget
from .core import CaimanSeriesExtensions, CNMFExtensions
from .cnmf_viz_gui import VizWidget
from tqdm import tqdm
from PyQt5 import QtWidgets, QtCore
from .evaluate_components import EvalComponentsWidgets


def _get_roi_colormap(self, n_colors) -> Tuple[List[np.ndarray], List[np.ndarray]]:
    """
    Get colormaps for both face and edges
    """
    edges = auto_colormap(
        n_colors=n_colors,
        cmap='hsv',
        output='mpl'
    )

    faces = auto_colormap(
        n_colors=n_colors,
        cmap='hsv',
        output='mpl',
        alpha=0.0
    )

    return edges, faces


class CNMFViewer:
    def __init__(self, batch_item: pd.Series, roi_type: str):
        self.batch_item = batch_item
        self.viewer = napari.Viewer(title="CNMF Visualization")

        self.viz_gui = VizWidget(cnmf_viewer=self, batch_item=batch_item)
        self.viewer.window.add_dock_widget(self.viz_gui, area='bottom', name="Visualization")
        #self.viz_gui.show()

        # Load correlation map first
        corr_img = batch_item.caiman.get_correlation_image()

        self.viewer.add_image(corr_img, name=f'corr: {batch_item["name"]}', colormap='gray')

        self.cnmf_obj = batch_item.cnmf.get_output()
        self.roi_type = roi_type

        self.napari_spatial_layer_good = None
        self.napari_spatial_layer_bad = None

        self.plot_spatial()
        self.plot_temporal()

    def plot_spatial(self):
        if self.roi_type == 'outline':
            coors = self.batch_item.cnmf.get_spatial_contour_coors(
                np.arange(0, self.cnmf_obj.estimates.A.shape[1])
            )

            edge_colors, face_colors = self.get_colors()

            self.spatial_layer: Shapes = self.viewer.add_shapes(
                data=coors,
                shape_type='polygon',
                edge_width=0.5,
                edge_color=edge_colors,
                face_color=face_colors,
                opacity=0.7,
                name='good components',
            )

        elif self.roi_type == 'mask':
            masks_good = self.batch_item.cnmf.get_spatial_masks(self.cnmf_obj.estimates.idx_components)
            masks_bad = self.batch_item.cnmf.get_spatial_masks(self.cnmf_obj.estimates.idx_components_bad)

            edge_colors, face_colors = self.get_colors(alpha_edge=0.0, alpha_face=0.5)
            for i in range(len(masks_good)):
                self.viewer.add_labels(data=masks_good[:, :, i], opacity=0.5)#, color=colors_good[i])

            # for i in range(len(masks_bad)):
            #     viewer.add_labels(data=masks_bad[:, :, i], color=masks_bad[i])

            # self.viewer.add_labels(
            #     data=masks_good,
            #     color=face_colors
            # )

            # viewer.add_labels(
            #     data=masks_bad,
            #     # color=colors_bad
            # )

    def update_visible_components(self):
        edge_colors, fc = self.get_colors()
        self.spatial_layer.edge_color = edge_colors
        self.temporal_layer.color = edge_colors

    def get_colors(self, alpha_edge=0.7, alpha_face=0.0):
        n_components = self.cnmf_obj.estimates.A.shape[1]
        colors = np.vstack(auto_colormap(
            n_colors=n_components,
            cmap='hsv',
            output='mpl',
            alpha=alpha_edge
        ))

        colors[self.cnmf_obj.estimates.idx_components, -1] = 0.8
        colors[self.cnmf_obj.estimates.idx_components_bad, -1] = 0.0

        face_colors = np.vstack(auto_colormap(
            n_colors=n_components,
            cmap='hsv',
            output='mpl',
            alpha=alpha_face
        ))

        return colors, face_colors

    def show_bad_components(self, b: bool):
        pass

    def plot_temporal(self):
        # Traces
        good_traces = self.cnmf_obj.estimates.C[self.cnmf_obj.estimates.idx_components]
        bad_traces = self.cnmf_obj.estimates.C[self.cnmf_obj.estimates.idx_components_bad]

        print("good traces", np.shape(good_traces))
        print("bad traces", np.shape(bad_traces))
        self.viewer1d = napari_plot.Viewer(show=False)
        qt_viewer = QtViewer(self.viewer1d)
        self.viewer1d.axis.y_label = "Intensity"
        self.viewer1d.axis.x_label = "Time"
        self.viewer1d.text_overlay.visible = True
        self.viewer1d.text_overlay.position = "top_right"
        self.viewer1d.text_overlay.font_size = 15

        n_pts = self.cnmf_obj.estimates.C.shape[1]
        n_lines = self.cnmf_obj.estimates.C.shape[0]
        xs = [np.linspace(0, n_pts, n_pts)]
        ys = []

        for i in range(n_lines):
            ys.append(self.cnmf_obj.estimates.C[i])

        self.temporal_layer = self.viewer1d.add_multi_line(
            data=dict(xs=xs, ys=ys),
            color=self.get_colors()[0],
            name='temporal'
        )

        self.viewer.window.add_dock_widget(qt_viewer, area="bottom", name="Line Widget")

        # Create layer for infinite line
        self.infline_layer = self.viewer1d.add_inf_line(
            data=[1], orientation="vertical", color="red", width=3, name="slider"
        )
        self.infline_layer.move(index=0, pos=[1000])
        self.viewer1d.add_layer(layer=self.infline_layer)
        self.viewer.dims.events.current_step.connect(self.update_slider)

    def update_slider(self, event):
        time = self.viewer.dims.current_step[0]
        print(time)
        self.infline_layer.move(index=0, pos=[time])
