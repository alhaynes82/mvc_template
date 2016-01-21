import sqlite3


class Model:

    def __init__(self, db_path, *args, **kwargs):
        self.db_path = db_path

    def _curcon(self):
        con = sqlite3.connect(self.db_path)
        cur = con.cursor()
        return con, cur

    def _fetchone(self, sql_statement):
        con, cur = self._curcon()

        with con:
            cur.execute(sql_statement)
            return cur.fetchone()

    def _fetchall(self, sql_statement):
        con, cur = self._curcon()

        with con:
            cur.execute(sql_statement)
            return cur.fetchall()

    def _insert(self, sql_statement, values):
        con, cur = self._curcon()

        with con:
            cur.execute(sql_statement, values)

    def _insertmany(self, sql_statements):
        # sql_statements = a list of lists, with each list being index 0 = sql, 1 = values.
        con, cur = self._curcon()

        for i in sql_statements:
            cur.execute(i[0], i[1])

    def _update(self, sql_statement, values):
        con, cur = self._curcon()

        with con:
            cur.execute(sql_statement, values)

    def _updatemany(self, sql_statements):
        # sql_statements = a list of lists, with each list being index 0 = sql, index 1 = values.
        con, cur = self._curcon()

        for i in sql_statements:
            cur.execute(i[0], i[1])