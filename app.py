from flask import Flask, request, abort
import json
import pymysql
 
DB_CONFIG = {
  "host": "localhost",
  "user": "root",
  "password": "",
  "database": "mhs",
  "cursorclass": pymysql.cursors.DictCursor,
  "autocommit": True
}
 
def get_connection():
  return pymysql.connect(**DB_CONFIG)
 
def validate_mhs(content):
  fields = ['npm', 'nama', 'angkatan', 'prodi', 'jenis_kelamin', 'email']
  for field in fields:
    if field not in content:
      return False
  return True
 
app = Flask(__name__)
 
@app.get("/mhs")
def get_mhs():
  try:
    conn = get_connection()
    with conn.cursor() as cur:
      cur.execute('SELECT * FROM mhs')
      mhs = cur.fetchall()
      return json.dumps(mhs)
  finally:
    conn.close()
 
@app.get("/mhs/<npm>")
def get_mhs_by_kode(npm):
  try:
    conn = get_connection()
    with conn.cursor() as cur:
      cur.execute('SELECT * FROM mhs WHERE npm = %s', [npm])
      mhs = cur.fetchone()
      if mhs is None:
        abort(404)
      return json.dumps(mhs)
  finally:
    conn.close()
 
@app.delete("/mhs/<npm>")
def delete_mhs(npm):
  try:
    conn = get_connection()
    with conn.cursor() as cur:
      affected = cur.execute('DELETE FROM mhs WHERE npm = %s', [npm])
      if affected == 0:
        abort(404)
      return "OK"
  finally:
    conn.close()
 
@app.post("/mhs")
def post_mhs():
  content = request.get_json()
  if not validate_mhs(content):
    abort(400)
  try:
    conn = get_connection()
    with conn.cursor() as cur:
      cur.execute('''
        INSERT INTO mhs VALUES (
          %(npm)s, %(nama)s, %(angkatan)s,
          %(prodi)s, %(jenis_kelamin)s, %(email)s
        )
      ''', content)
    return "Created", 201
  finally:
    conn.close()
 
@app.put("/mhs/<npm>")
def put_mhs(npm):
  # cek apakah mhs dgn npm tsb ada, jk tdk ada, abort(404)
  content = request.get_json()
  if not validate_mhs(content):
    abort(400)

  try:
    conn = get_connection()
    with conn.cursor() as cur:
      cur.execute('SELECT npm FROM mhs WHERE npm = %s', [npm])
      mhs = cur.fetchone()
      if mhs is None:
        abort(404)

      # lakukan update seluruh kolom (replace data lama)
      cur.execute('''
        UPDATE mhs
        SET nama = %(nama)s,
            angkatan = %(angkatan)s,
            prodi = %(prodi)s,
            jenis_kelamin = %(jenis_kelamin)s,
            email = %(email)s
        WHERE npm = %(npm)s
      ''', content)

      return 'OK'
  finally:
    conn.close()
 
@app.patch("/mhs/<npm>")
def patch_mhs(npm):
  # cek apakah mhs dgn npm tsb ada, jk tdk ada, abort(404)
  content = request.get_json()
  try:
    conn = get_connection()
    with conn.cursor() as cur:
      cur.execute('SELECT * FROM mhs WHERE npm = %s', [npm])
      mhs = cur.fetchone()
      if mhs is None:
        abort(404)

      # buat query update dinamis hanya untuk field yang dikirim
      fields = []
      values = []
      for key, value in content.items():
        if key in ['nama', 'angkatan', 'prodi', 'jenis_kelamin', 'email']:
          fields.append(f"{key} = %s")
          values.append(value)

      if not fields:
        abort(400)

      values.append(npm)
      sql = f"UPDATE mhs SET {', '.join(fields)} WHERE npm = %s"
      cur.execute(sql, values)

      return 'OK'
  finally:
    conn.close()
 
if __name__ == '__main__':
  app.run()
