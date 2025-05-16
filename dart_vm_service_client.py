import grpc
import dart_vm_service_pb2
import dart_vm_service_pb2_grpc

class DartVmServiceClient:
    def __init__(self, server_address="localhost:50051"):
        """
        Initialize the client with the server address.
        
        Args:
            server_address (str): The address of the gRPC server in format 'host:port'
        """
        self.channel = grpc.insecure_channel(server_address)
        self.stub = dart_vm_service_pb2_grpc.DartVmServiceStub(self.channel)
    
    def connect(self, vm_service_uri):
        """Connect to a Flutter app VM service."""
        request = dart_vm_service_pb2.ConnectRequest(vm_service_uri=vm_service_uri)
        return self.stub.Connect(request)
    
    def toggle_debug_paint(self, enable=True):
        """Enable or disable debug painting."""
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleDebugPaint(request)
    
    def close(self):
        """Close the gRPC channel."""
        self.channel.close()

    # Debug Visualization Toggles
    def toggle_repaint_rainbow(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleRepaintRainbow(request)

    def toggle_performance_overlay(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.TogglePerformanceOverlay(request)

    def toggle_baseline_painting(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleBaselinePainting(request)

    def toggle_debug_banner(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleDebugBanner(request)

    def toggle_structured_errors(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleStructuredErrors(request)

    def toggle_oversized_images(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleOversizedImages(request)

    def toggle_disable_physical_shape_layers(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleDisablePhysicalShapeLayers(request)

    def toggle_disable_opacity_layers(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleDisableOpacityLayers(request)

    # Profiling Toggles
    def toggle_profile_widget_builds(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleProfileWidgetBuilds(request)

    def toggle_profile_user_widget_builds(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleProfileUserWidgetBuilds(request)

    def toggle_profile_render_object_paints(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleProfileRenderObjectPaints(request)

    def toggle_profile_render_object_layouts(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleProfileRenderObjectLayouts(request)

    def toggle_profile_platform_channels(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleProfilePlatformChannels(request)

    # Inspector Control Toggles
    def toggle_inspector(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleInspector(request)

    def toggle_track_rebuild_widgets(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleTrackRebuildWidgets(request)

    def toggle_track_repaint_widgets(self, enable=True):
        request = dart_vm_service_pb2.ToggleRequest(enable=enable)
        return self.stub.ToggleTrackRepaintWidgets(request)

    # Screen Info
    def get_display_refresh_rate(self, view_id):
        request = dart_vm_service_pb2.ViewIdRequest(view_id=view_id)
        return self.stub.GetDisplayRefreshRate(request)

    def list_views(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.ListViews(request)

    # Dump Tree Methods
    def dump_widget_tree(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.DumpWidgetTree(request)

    def dump_layer_tree(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.DumpLayerTree(request)

    def dump_render_tree(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.DumpRenderTree(request)

    def dump_semantics_tree_in_traversal_order(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.DumpSemanticsTreeInTraversalOrder(request)

    def dump_semantics_tree_in_inverse_hit_test_order(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.DumpSemanticsTreeInInverseHitTestOrder(request)

    def dump_focus_tree(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.DumpFocusTree(request)

    # Frame and Timing
    def set_time_dilation(self, value):
        request = dart_vm_service_pb2.DoubleValueRequest(value=value)
        return self.stub.SetTimeDilation(request)

    def did_send_first_frame_event(self, value): # Assuming boolean
        request = dart_vm_service_pb2.BoolValueRequest(value=value)
        return self.stub.DidSendFirstFrameEvent(request)

    def did_send_first_frame_rasterized_event(self, value): # Assuming string
        request = dart_vm_service_pb2.StringValueRequest(value=value)
        return self.stub.DidSendFirstFrameRasterizedEvent(request)

    # Asset and App Management
    def evict_assets(self, value): # Assuming string (asset path or similar)
        request = dart_vm_service_pb2.StringValueRequest(value=value)
        return self.stub.EvictAssets(request)

    def reassemble(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.Reassemble(request)

    def exit_app(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.ExitApp(request)

    # Configuration Methods
    def set_vm_service_uri(self, value):
        request = dart_vm_service_pb2.StringValueRequest(value=value)
        return self.stub.SetVmServiceUri(request)

    def set_dev_tools_server_address(self, value):
        request = dart_vm_service_pb2.StringValueRequest(value=value)
        return self.stub.SetDevToolsServerAddress(request)

    def set_platform_override(self, value): # e.g., "iOS", "android"
        request = dart_vm_service_pb2.StringValueRequest(value=value)
        return self.stub.SetPlatformOverride(request)

    def set_brightness_override(self, value): # e.g., "light", "dark"
        request = dart_vm_service_pb2.StringValueRequest(value=value)
        return self.stub.SetBrightnessOverride(request)

    # Pub Root Directory Management
    def set_pub_root_directories(self, values):
        request = dart_vm_service_pb2.StringListRequest(values=values)
        return self.stub.SetPubRootDirectories(request)

    def add_pub_root_directories(self, values):
        request = dart_vm_service_pb2.StringListRequest(values=values)
        return self.stub.AddPubRootDirectories(request)

    def remove_pub_root_directories(self, values):
        request = dart_vm_service_pb2.StringListRequest(values=values)
        return self.stub.RemovePubRootDirectories(request)

    def get_pub_root_directories(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.GetPubRootDirectories(request)

    # Widget Interaction (Flutter Finder)
    def tap_widget_by_key(self, key_value):
        request = dart_vm_service_pb2.StringValueRequest(value=key_value)
        return self.stub.TapWidgetByKey(request)

    def tap_widget_by_text(self, text):
        request = dart_vm_service_pb2.StringValueRequest(value=text)
        return self.stub.TapWidgetByText(request)

    def tap_widget_by_type(self, widget_type):
        request = dart_vm_service_pb2.StringValueRequest(value=widget_type)
        return self.stub.TapWidgetByType(request)

    def tap_widget_by_tooltip(self, tooltip_text):
        request = dart_vm_service_pb2.StringValueRequest(value=tooltip_text)
        return self.stub.TapWidgetByTooltip(request)

    def tap_widget_by_ancestor_and_descendant(self, ancestor_type, descendant_type):
        request = dart_vm_service_pb2.AncestorDescendantRequest(ancestor_type=ancestor_type, descendant_type=descendant_type)
        return self.stub.TapWidgetByAncestorAndDescendant(request)

    def enter_text(self, key_value, text):
        request = dart_vm_service_pb2.EnterTextRequest(key_value=key_value, text=text)
        return self.stub.EnterText(request)
        
    def is_widget_tree_ready(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.IsWidgetTreeReady(request)

    def is_widget_creation_tracked(self):
        request = dart_vm_service_pb2.EmptyRequest()
        return self.stub.IsWidgetCreationTracked(request)

    def get_root_widget(self, object_group):
        request = dart_vm_service_pb2.ObjectGroupRequest(object_group=object_group)
        return self.stub.GetRootWidget(request)

    def get_root_widget_summary_tree(self, object_group):
        request = dart_vm_service_pb2.ObjectGroupRequest(object_group=object_group)
        return self.stub.GetRootWidgetSummaryTree(request)

    def get_root_widget_summary_tree_with_previews(self, object_group):
        request = dart_vm_service_pb2.ObjectGroupRequest(object_group=object_group)
        return self.stub.GetRootWidgetSummaryTreeWithPreviews(request)

    def get_selected_widget(self, object_group, previous_selection_id=None):
        request = dart_vm_service_pb2.SelectedWidgetRequest(object_group=object_group, previous_selection_id=previous_selection_id)
        return self.stub.GetSelectedWidget(request)

    def get_selected_summary_widget(self, object_group, previous_selection_id=None):
        request = dart_vm_service_pb2.SelectedWidgetRequest(object_group=object_group, previous_selection_id=previous_selection_id)
        return self.stub.GetSelectedSummaryWidget(request)

    def set_selection_by_id(self, object_group, object_id):
        request = dart_vm_service_pb2.SelectionByIdRequest(object_group=object_group, object_id=object_id)
        return self.stub.SetSelectionById(request)

    # Object Management
    def dispose_all_groups(self, object_group):
        request = dart_vm_service_pb2.ObjectGroupRequest(object_group=object_group)
        return self.stub.DisposeAllGroups(request)

    def dispose_group(self, object_group):
        request = dart_vm_service_pb2.ObjectGroupRequest(object_group=object_group)
        return self.stub.DisposeGroup(request)

    def dispose_id(self, object_group, object_id):
        request = dart_vm_service_pb2.DisposeIdRequest(object_group=object_group, object_id=object_id)
        return self.stub.DisposeId(request)

    # Widget Details
    def get_parent_chain(self, object_group, widget_id):
        request = dart_vm_service_pb2.WidgetRequest(object_group=object_group, widget_id=widget_id)
        return self.stub.GetParentChain(request)

    def get_properties(self, object_group, widget_id):
        request = dart_vm_service_pb2.WidgetRequest(object_group=object_group, widget_id=widget_id)
        return self.stub.GetProperties(request)

    def get_children(self, object_group, widget_id):
        request = dart_vm_service_pb2.WidgetRequest(object_group=object_group, widget_id=widget_id)
        return self.stub.GetChildren(request)

    def get_children_summary_tree(self, object_group, widget_id):
        request = dart_vm_service_pb2.WidgetRequest(object_group=object_group, widget_id=widget_id)
        return self.stub.GetChildrenSummaryTree(request)

    def get_children_details_subtree(self, object_group, widget_id):
        request = dart_vm_service_pb2.WidgetRequest(object_group=object_group, widget_id=widget_id)
        return self.stub.GetChildrenDetailsSubtree(request)

    def get_details_subtree(self, object_group, widget_id, subtree_depth):
        request = dart_vm_service_pb2.DetailSubtreeRequest(object_group=object_group, widget_id=widget_id, subtree_depth=subtree_depth)
        return self.stub.GetDetailsSubtree(request)

    # Screenshot and Layout
    def screenshot(self, widget_id=None, width=None, height=None, margin=None, max_pixel_ratio=None, debug_paint=False):
        request = dart_vm_service_pb2.ScreenshotRequest(
            widget_id=widget_id,
            width=width,
            height=height,
            margin=margin,
            max_pixel_ratio=max_pixel_ratio,
            debug_paint=debug_paint
        )
        return self.stub.Screenshot(request)

    def get_layout_explorer_node(self, object_group, widget_id, subtree_depth):
        request = dart_vm_service_pb2.LayoutExplorerRequest(
            object_group=object_group,
            widget_id=widget_id,
            subtree_depth=subtree_depth
        )
        return self.stub.GetLayoutExplorerNode(request)

    def set_flex_fit(self, widget_id, flex_fit):
        request = dart_vm_service_pb2.FlexFitRequest(
            widget_id=widget_id,
            flex_fit=flex_fit
        )
        return self.stub.SetFlexFit(request)

    def set_flex_factor(self, widget_id, flex_factor):
        request = dart_vm_service_pb2.FlexFactorRequest(
            widget_id=widget_id,
            flex_factor=flex_factor
        )
        return self.stub.SetFlexFactor(request)

    def set_flex_properties(self, widget_id, main_axis_alignment, cross_axis_alignment):
        request = dart_vm_service_pb2.FlexPropertiesRequest(
            widget_id=widget_id,
            main_axis_alignment=main_axis_alignment,
            cross_axis_alignment=cross_axis_alignment
        )
        return self.stub.SetFlexProperties(request)

    def enter_text_by_key(self, key_value, text):
        request = dart_vm_service_pb2.EnterTextKeyRequest(key_value=key_value, text=text)
        return self.stub.EnterTextByKey(request)

    def enter_text_by_type(self, widget_type, text):
        request = dart_vm_service_pb2.EnterTextTypeRequest(widget_type=widget_type, text=text)
        return self.stub.EnterTextByType(request)

    def enter_text_by_text(self, widget_text, text):
        request = dart_vm_service_pb2.EnterTextTextRequest(widget_text=widget_text, text=text)
        return self.stub.EnterTextByText(request)

    def enter_text_by_tooltip(self, tooltip, text):
        request = dart_vm_service_pb2.EnterTextTooltipRequest(tooltip=tooltip, text=text)
        return self.stub.EnterTextByTooltip(request)

    def enter_text_by_ancestor_and_descendant(self, ancestor_type, descendant_type, text):
        request = dart_vm_service_pb2.EnterTextAncestorDescendantRequest(
            ancestor_type=ancestor_type,
            descendant_type=descendant_type,
            text=text
        )
        return self.stub.EnterTextByAncestorAndDescendant(request)

    # Basic scrolling
    def scroll_down_by_key(self, key_value):
        request = dart_vm_service_pb2.StringValueRequest(value=key_value)
        return self.stub.ScrollDownByKey(request)

    def scroll_down_by_type(self, widget_type):
        request = dart_vm_service_pb2.StringValueRequest(value=widget_type)
        return self.stub.ScrollDownByType(request)

    def scroll_down_by_text(self, text):
        request = dart_vm_service_pb2.StringValueRequest(value=text)
        return self.stub.ScrollDownByText(request)

    def scroll_down_by_tooltip(self, tooltip):
        request = dart_vm_service_pb2.StringValueRequest(value=tooltip)
        return self.stub.ScrollDownByTooltip(request)

    def scroll_down_by_ancestor_and_descendant(self, ancestor_type, descendant_type):
        request = dart_vm_service_pb2.AncestorDescendantRequest(
            ancestor_type=ancestor_type,
            descendant_type=descendant_type
        )
        return self.stub.ScrollDownByAncestorAndDescendant(request)

    def scroll_up_by_key(self, key_value):
        request = dart_vm_service_pb2.StringValueRequest(value=key_value)
        return self.stub.ScrollUpByKey(request)

    def scroll_up_by_type(self, widget_type):
        request = dart_vm_service_pb2.StringValueRequest(value=widget_type)
        return self.stub.ScrollUpByType(request)

    def scroll_up_by_text(self, text):
        request = dart_vm_service_pb2.StringValueRequest(value=text)
        return self.stub.ScrollUpByText(request)

    def scroll_up_by_tooltip(self, tooltip):
        request = dart_vm_service_pb2.StringValueRequest(value=tooltip)
        return self.stub.ScrollUpByTooltip(request)

    def scroll_up_by_ancestor_and_descendant(self, ancestor_type, descendant_type):
        request = dart_vm_service_pb2.AncestorDescendantRequest(
            ancestor_type=ancestor_type,
            descendant_type=descendant_type
        )
        return self.stub.ScrollUpByAncestorAndDescendant(request)

    # Extended scrolling with more parameters
    def scroll_down_by_key_extended(self, key_value, dx=0, dy=100, duration_microseconds=300000, frequency=60):
        request = dart_vm_service_pb2.ScrollKeyRequest(
            key_value=key_value,
            dx=dx,
            dy=dy,
            duration_microseconds=duration_microseconds,
            frequency=frequency
        )
        return self.stub.ScrollDownByKeyExtended(request)

    def scroll_down_by_type_extended(self, widget_type, dx=0, dy=100, duration_microseconds=300000, frequency=60):
        request = dart_vm_service_pb2.ScrollTypeRequest(
            widget_type=widget_type,
            dx=dx,
            dy=dy,
            duration_microseconds=duration_microseconds,
            frequency=frequency
        )
        return self.stub.ScrollDownByTypeExtended(request)

    def scroll_down_by_text_extended(self, text, dx=0, dy=100, duration_microseconds=300000, frequency=60):
        request = dart_vm_service_pb2.ScrollTextRequest(
            text=text,
            dx=dx,
            dy=dy,
            duration_microseconds=duration_microseconds,
            frequency=frequency
        )
        return self.stub.ScrollDownByTextExtended(request)
    
    def scroll_up_by_key_extended(self, key_value, dx=0, dy=-100, duration_microseconds=300000, frequency=60):
        request = dart_vm_service_pb2.ScrollKeyRequest(
            key_value=key_value,
            dx=dx,
            dy=dy,
            duration_microseconds=duration_microseconds,
            frequency=frequency
        )
        return self.stub.ScrollUpByKeyExtended(request)

    # Scroll into view methods
    def scroll_into_view_by_key(self, key_value, alignment=0):
        request = dart_vm_service_pb2.ScrollIntoViewKeyRequest(
            key_value=key_value,
            alignment=alignment
        )
        return self.stub.ScrollIntoViewByKey(request)

    def scroll_into_view_by_type(self, widget_type, alignment=0):
        request = dart_vm_service_pb2.ScrollIntoViewTypeRequest(
            widget_type=widget_type,
            alignment=alignment
        )
        return self.stub.ScrollIntoViewByType(request)

    def scroll_into_view_by_text(self, text, alignment=0):
        request = dart_vm_service_pb2.ScrollIntoViewTextRequest(
            text=text,
            alignment=alignment
        )
        return self.stub.ScrollIntoViewByText(request)

    def scroll_into_view_by_tooltip(self, tooltip, alignment=0):
        request = dart_vm_service_pb2.ScrollIntoViewTooltipRequest(
            tooltip=tooltip,
            alignment=alignment
        )
        return self.stub.ScrollIntoViewByTooltip(request)

    def scroll_into_view_by_ancestor_and_descendant(self, ancestor_type, descendant_type, alignment=0):
        request = dart_vm_service_pb2.ScrollIntoViewAncestorDescendantRequest(
            ancestor_type=ancestor_type,
            descendant_type=descendant_type,
            alignment=alignment
        )
        return self.stub.ScrollIntoViewByAncestorAndDescendant(request)


# Example usage
if __name__ == "__main__":
    # Create a client
    client = DartVmServiceClient()
    
    try:
        # Connect to a Flutter app
        print("Connecting to Flutter app...")
        response = client.connect("ws://127.0.0.1:50505/ws")
        print(f"Connection status: {response.success}, Message: {response.message}")
        
        if response.success:
            # Get the widget tree
            print("\nGetting widget tree...")
            widget_tree = client.get_root_widget_summary_tree_with_previews("flutter")
            print(f"Widget tree retrieved: {widget_tree.success}")
            
            # Tap a widget by key
            print("\nTapping a widget by key...")
            tap_response = client.tap_widget_by_key("increment_button")
            print(f"Tap response: {tap_response.success}, {tap_response.message}")
            
            # Enter text
            print("\nEntering text...")
            text_response = client.enter_text("search_field", "Hello Flutter!")
            print(f"Text entry response: {text_response.success}, {text_response.message}")
            
            # Toggle debug features
            print("\nToggling debug features...")
            client.toggle_debug_paint(enable=False)
            print("  Debug paint disabled.")
            client.toggle_performance_overlay(enable=False)
            print("  Performance overlay disabled.")
            client.toggle_repaint_rainbow(enable=False)
            print("  Repaint rainbow disabled.")
        
    except grpc.RpcError as e:
        print(f"RPC Error: {e.code()}, {e.details()}")
    
    finally:
        # Close the channel
        client.close()
        print("\nClient connection closed") 