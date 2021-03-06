#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Sep 29 18:36:19 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from equalize_chains import equalize_chains  # grc-generated hier_block
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from ofdm_m_channel_sync import ofdm_m_channel_sync  # grc-generated hier_block
from ofdm_packet_sync import ofdm_packet_sync  # grc-generated hier_block
from optparse import OptionParser
import doa
import math
import ofdm
import ofdm.gen_preamble as gp
import ofdm.packet_process as pp
import pmt
import sip


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.occupied_carriers = occupied_carriers = 200
        self.fft_len = fft_len = 512
        self.view = view = False
        self.rcvd_pktq = rcvd_pktq = gr.msg_queue()
        self.modulation = modulation = 'bpsk'
        self.mods = mods = {"bpsk": 2, "qpsk": 4, "8psk": 8, "qam8": 8, "qam16": 16, "qam64": 64, "qam256": 256}
        self.bw = bw = (float(occupied_carriers) / float(fft_len)) / 2.0
        self.zeros_on_left = zeros_on_left = int(math.ceil((fft_len - occupied_carriers)/2.0))
        self.win = win = [1 for i in range(fft_len )]
        self.watcher = watcher = pp._queue_watcher_thread(rcvd_pktq,view)
        self.tb = tb = bw*0.08
        self.samp_rate = samp_rate = 10000000/2
        self.rotated_const = rotated_const = gp.gen_framer_info(modulation)
        self.phgain = phgain = 0.25
        self.max_fft_shift = max_fft_shift = 4
        self.ks0 = ks0 = gp.gen_preamble_data(fft_len , occupied_carriers)
        self.cp_len = cp_len = 128
        self.arity = arity = mods[modulation]

        ##################################################
        # Blocks
        ##################################################
        self.twinrx_usrp_source_0 = doa.twinrx_usrp_source(
            samp_rate=samp_rate,
            center_freq=2.45e9,
            gain=60,
            sources=4,
            addresses="addr=192.168.50.2"
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	20, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(True)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	4 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(True)
        self.qtgui_const_sink_x_0.enable_grid(True)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)
        
        if not True:
          self.qtgui_const_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 1, 2, 3, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(4):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.phase_correct_hier_1 = doa.phase_correct_hier(
            num_ports=4,
            config_filename='/tmp/measure_X310_TwinRX_phase_offsets_245.cfg',
        )
        self.ofdm_packet_sync_0 = ofdm_packet_sync(
            cp_len=cp_len,
            fft_len=fft_len,
        )
        self.ofdm_ofdm_mrx_frame_sink_0 = ofdm.ofdm_mrx_frame_sink(rotated_const, range(arity), rcvd_pktq, occupied_carriers, phgain, phgain*phgain /4.0, 4)
        self.ofdm_m_channel_sync_0 = ofdm_m_channel_sync(
            cp_len=cp_len,
            fft_len=fft_len,
            max_fft_shift=max_fft_shift,
            occupied_carriers=occupied_carriers,
        )
        self.ofdm_eadf_doa_0 = ofdm.eadf_doa('/home/travis/Dropbox/PHD/WiFiUS/doa/gnuradio/gr-ofdm/matlab_code/data.mat', 4, 256)
        self.fft_filter_xxx_0_0_0_0 = filter.fft_filter_ccc(1, (filter.firdes.low_pass (1.0, 1.0, bw+tb, tb, filter.firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_0_0_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0_0_0 = filter.fft_filter_ccc(1, (filter.firdes.low_pass (1.0, 1.0, bw+tb, tb, filter.firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_0_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0_0 = filter.fft_filter_ccc(1, (filter.firdes.low_pass (1.0, 1.0, bw+tb, tb, filter.firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_0_0.declare_sample_delay(0)
        self.fft_filter_xxx_0 = filter.fft_filter_ccc(1, (filter.firdes.low_pass (1.0, 1.0, bw+tb, tb, filter.firdes.WIN_HAMMING)), 1)
        self.fft_filter_xxx_0.declare_sample_delay(0)
        self.equalize_chains_0 = equalize_chains(
            cp_len=cp_len,
            fft_len=fft_len,
            nports=4,
            occupied_carriers=occupied_carriers,
        )
        self.blocks_vector_to_stream_0_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, occupied_carriers)
        self.blocks_vector_to_stream_0_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, occupied_carriers)
        self.blocks_vector_to_stream_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, occupied_carriers)
        self.blocks_vector_to_stream_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, occupied_carriers)
        self.blocks_message_debug_0 = blocks.message_debug()

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ofdm_ofdm_mrx_frame_sink_0, 'packet'), (self.blocks_message_debug_0, 'store'))    
        self.msg_connect((self.ofdm_ofdm_mrx_frame_sink_0, 'header_dfe'), (self.ofdm_eadf_doa_0, 'Chan_Est'))    
        self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.qtgui_const_sink_x_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0_0_0, 0), (self.qtgui_const_sink_x_0, 1))    
        self.connect((self.blocks_vector_to_stream_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0, 2))    
        self.connect((self.blocks_vector_to_stream_0_0_0_0_0_0, 0), (self.qtgui_const_sink_x_0, 3))    
        self.connect((self.equalize_chains_0, 0), (self.ofdm_ofdm_mrx_frame_sink_0, 1))    
        self.connect((self.equalize_chains_0, 1), (self.ofdm_ofdm_mrx_frame_sink_0, 2))    
        self.connect((self.equalize_chains_0, 2), (self.ofdm_ofdm_mrx_frame_sink_0, 3))    
        self.connect((self.equalize_chains_0, 3), (self.ofdm_ofdm_mrx_frame_sink_0, 4))    
        self.connect((self.fft_filter_xxx_0, 0), (self.ofdm_packet_sync_0, 0))    
        self.connect((self.fft_filter_xxx_0_0, 0), (self.ofdm_m_channel_sync_0, 3))    
        self.connect((self.fft_filter_xxx_0_0_0, 0), (self.ofdm_m_channel_sync_0, 4))    
        self.connect((self.fft_filter_xxx_0_0_0_0, 0), (self.ofdm_m_channel_sync_0, 5))    
        self.connect((self.ofdm_eadf_doa_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.ofdm_m_channel_sync_0, 5), (self.equalize_chains_0, 5))    
        self.connect((self.ofdm_m_channel_sync_0, 0), (self.equalize_chains_0, 0))    
        self.connect((self.ofdm_m_channel_sync_0, 1), (self.equalize_chains_0, 1))    
        self.connect((self.ofdm_m_channel_sync_0, 2), (self.equalize_chains_0, 2))    
        self.connect((self.ofdm_m_channel_sync_0, 3), (self.equalize_chains_0, 3))    
        self.connect((self.ofdm_m_channel_sync_0, 4), (self.equalize_chains_0, 4))    
        self.connect((self.ofdm_m_channel_sync_0, 6), (self.ofdm_ofdm_mrx_frame_sink_0, 0))    
        self.connect((self.ofdm_ofdm_mrx_frame_sink_0, 0), (self.blocks_vector_to_stream_0_0_0, 0))    
        self.connect((self.ofdm_ofdm_mrx_frame_sink_0, 1), (self.blocks_vector_to_stream_0_0_0_0, 0))    
        self.connect((self.ofdm_ofdm_mrx_frame_sink_0, 2), (self.blocks_vector_to_stream_0_0_0_0_0, 0))    
        self.connect((self.ofdm_ofdm_mrx_frame_sink_0, 3), (self.blocks_vector_to_stream_0_0_0_0_0_0, 0))    
        self.connect((self.ofdm_packet_sync_0, 1), (self.ofdm_m_channel_sync_0, 1))    
        self.connect((self.ofdm_packet_sync_0, 0), (self.ofdm_m_channel_sync_0, 0))    
        self.connect((self.ofdm_packet_sync_0, 2), (self.ofdm_m_channel_sync_0, 2))    
        self.connect((self.phase_correct_hier_1, 0), (self.fft_filter_xxx_0, 0))    
        self.connect((self.phase_correct_hier_1, 1), (self.fft_filter_xxx_0_0, 0))    
        self.connect((self.phase_correct_hier_1, 2), (self.fft_filter_xxx_0_0_0, 0))    
        self.connect((self.phase_correct_hier_1, 3), (self.fft_filter_xxx_0_0_0_0, 0))    
        self.connect((self.twinrx_usrp_source_0, 0), (self.phase_correct_hier_1, 0))    
        self.connect((self.twinrx_usrp_source_0, 1), (self.phase_correct_hier_1, 1))    
        self.connect((self.twinrx_usrp_source_0, 2), (self.phase_correct_hier_1, 2))    
        self.connect((self.twinrx_usrp_source_0, 3), (self.phase_correct_hier_1, 3))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_bw((float(self.occupied_carriers) / float(self.fft_len)) / 2.0)
        self.set_zeros_on_left(int(math.ceil((self.fft_len - self.occupied_carriers)/2.0)))
        self.ofdm_m_channel_sync_0.set_occupied_carriers(self.occupied_carriers)
        self.set_ks0(gp.gen_preamble_data(self.fft_len , self.occupied_carriers))
        self.equalize_chains_0.set_occupied_carriers(self.occupied_carriers)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_bw((float(self.occupied_carriers) / float(self.fft_len)) / 2.0)
        self.set_zeros_on_left(int(math.ceil((self.fft_len - self.occupied_carriers)/2.0)))
        self.set_win([1 for i in range(self.fft_len )])
        self.ofdm_packet_sync_0.set_fft_len(self.fft_len)
        self.ofdm_m_channel_sync_0.set_fft_len(self.fft_len)
        self.set_ks0(gp.gen_preamble_data(self.fft_len , self.occupied_carriers))
        self.equalize_chains_0.set_fft_len(self.fft_len)

    def get_view(self):
        return self.view

    def set_view(self, view):
        self.view = view
        self.set_watcher(pp._queue_watcher_thread(self.rcvd_pktq,self.view))

    def get_rcvd_pktq(self):
        return self.rcvd_pktq

    def set_rcvd_pktq(self, rcvd_pktq):
        self.rcvd_pktq = rcvd_pktq
        self.set_watcher(pp._queue_watcher_thread(self.rcvd_pktq,self.view))

    def get_modulation(self):
        return self.modulation

    def set_modulation(self, modulation):
        self.modulation = modulation
        self.set_rotated_const(gp.gen_framer_info(self.modulation))
        self.set_arity(self.mods[self.modulation])

    def get_mods(self):
        return self.mods

    def set_mods(self, mods):
        self.mods = mods
        self.set_arity(self.mods[self.modulation])

    def get_bw(self):
        return self.bw

    def set_bw(self, bw):
        self.bw = bw
        self.set_tb(self.bw*0.08)
        self.fft_filter_xxx_0_0_0_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))
        self.fft_filter_xxx_0_0_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))
        self.fft_filter_xxx_0_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))
        self.fft_filter_xxx_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))

    def get_zeros_on_left(self):
        return self.zeros_on_left

    def set_zeros_on_left(self, zeros_on_left):
        self.zeros_on_left = zeros_on_left

    def get_win(self):
        return self.win

    def set_win(self, win):
        self.win = win

    def get_watcher(self):
        return self.watcher

    def set_watcher(self, watcher):
        self.watcher = watcher

    def get_tb(self):
        return self.tb

    def set_tb(self, tb):
        self.tb = tb
        self.fft_filter_xxx_0_0_0_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))
        self.fft_filter_xxx_0_0_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))
        self.fft_filter_xxx_0_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))
        self.fft_filter_xxx_0.set_taps((filter.firdes.low_pass (1.0, 1.0, self.bw+self.tb, self.tb, filter.firdes.WIN_HAMMING)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.twinrx_usrp_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_rotated_const(self):
        return self.rotated_const

    def set_rotated_const(self, rotated_const):
        self.rotated_const = rotated_const

    def get_phgain(self):
        return self.phgain

    def set_phgain(self, phgain):
        self.phgain = phgain

    def get_max_fft_shift(self):
        return self.max_fft_shift

    def set_max_fft_shift(self, max_fft_shift):
        self.max_fft_shift = max_fft_shift
        self.ofdm_m_channel_sync_0.set_max_fft_shift(self.max_fft_shift)

    def get_ks0(self):
        return self.ks0

    def set_ks0(self, ks0):
        self.ks0 = ks0

    def get_cp_len(self):
        return self.cp_len

    def set_cp_len(self, cp_len):
        self.cp_len = cp_len
        self.ofdm_packet_sync_0.set_cp_len(self.cp_len)
        self.ofdm_m_channel_sync_0.set_cp_len(self.cp_len)
        self.equalize_chains_0.set_cp_len(self.cp_len)

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
