# Copyright (c) 2024, Tesar Rahmat Maulana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class Testimoni(Document):
    def before_insert(self):
        # Memeriksa apakah siswa sudah mengirimkan testimoni hari ini
        existing_testimoni = frappe.get_all('Testimoni', filters={
            'siswa': self.siswa,  # Pastikan field 'siswa' ada dalam Doctype Testimoni
            'creation': ['like', nowdate() + '%']  # Mencocokkan tanggal hari ini
        })
        
        if existing_testimoni:
            frappe.throw('Anda sudah mengirimkan testimoni hari ini. Mohon tunggu besok untuk mengirimkan testimoni lagi.')

        # Memeriksa apakah guru sudah mengirimkan testimoni hari ini
        existing_testimoni2 = frappe.get_all('Testimoni', filters={
            'guru': self.guru,  # Pastikan field '' ada dalam Doctype Testimoni
            'creation': ['like', nowdate() + '%']  # Mencocokkan tanggal hari ini
        })
        
        if existing_testimoni2:
            frappe.throw('Anda sudah mengirimkan testimoni hari ini. Mohon tunggu besok untuk mengirimkan testimoni lagi.')