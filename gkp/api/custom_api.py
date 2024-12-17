import frappe

@frappe.whitelist(allow_guest=True)
def get_unique_dates():
    unique_dates = frappe.db.sql("""
        SELECT DISTINCT tanggal
        FROM `tabTestimoni`
        ORDER BY tanggal
    """, as_dict=True)
    return unique_dates

@frappe.whitelist(allow_guest=True)
def get_testimoni_summary():
    """
    Mengambil jumlah siswa, guru, dan tamu yang memberikan testimoni, dipisahkan berdasarkan tanggal.
    """
    result = frappe.db.sql("""
        SELECT 
            tanggal,
            SUM(CASE WHEN status = 'Siswa' THEN 1 ELSE 0 END) AS jumlah_siswa,
            SUM(CASE WHEN status = 'Guru' THEN 1 ELSE 0 END) AS jumlah_guru,
            SUM(CASE WHEN status = 'Tamu' THEN 1 ELSE 0 END) AS jumlah_tamu
        FROM `tabTestimoni`
        GROUP BY tanggal
        ORDER BY tanggal DESC
    """, as_dict=True)
    
    return result

@frappe.whitelist(allow_guest=True)
def get_testimoni_summary2():
    """
    Mengambil data testimoni dengan menampilkan nama siswa, guru, atau tamu berdasarkan kondisi.
    """
    result = frappe.db.sql("""
        SELECT 
            t.name,
            t.status,
            t.siswa,
            t.guru,
            t.tamu,
            t.instansi,
            t.tanggal,
            t.rating,
            t.testimoni,
            CASE
                WHEN t.siswa IS NOT NULL THEN (SELECT nama FROM `tabSiswa` WHERE name = t.siswa)
                WHEN t.guru IS NOT NULL THEN (SELECT nama FROM `tabGuru` WHERE name = t.guru)
                ELSE t.tamu
            END AS nama
        FROM `tabTestimoni` t
        ORDER BY t.tanggal DESC
        LIMIT 10
    """, as_dict=True)

    return result

