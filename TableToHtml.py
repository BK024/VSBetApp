# As deployed to BK024.pythonanywhere.com with version 0.8.

"""
Class that holds a table (in the form of python objects) and translates those to html code that is a table.
Will be hardcoded for translating the first bet to a table. But will be made more flexible.
TODO Make flexible.
"""

from collections import OrderedDict as OD

class Table:
    def __init__(self, header_OD, rows, name="first_bet", row_size=5, num_rows=4):
        self.size_tuple = (row_size, num_rows)
        self.name = name
        self.headers_dict = header_OD if header_OD else OD([("Position", 8), ("Participant", 20), ("Candidate (%)", 20), ("Payout (profit)", 10)])
        self.rows = rows

    def set_rows(self, row_list):
        assert len(row_list) == self.size_tuple[1]
        self.rows = row_list

    def translate_to_html_str(self):
        table_tag_open = "<table>"
        table_tag_close = "</table>"
        table_headers = "<tr>{}</tr>".format(self.make_headers_html())
        table_rows = self.make_rows_html()
        return table_tag_open + table_headers + table_rows + table_tag_close

    def make_headers_html(self):
        headers_html_string = ""
        for header in self.headers_dict.keys():
            headers_html_string = headers_html_string + "<th>{}</th>".format(header)
        return headers_html_string

    def make_rows_html(self):
        row_html_string = ""
        for row in self.rows:
            row_html_string = row_html_string +"<tr>"
            for k, v in row.items():
                v = self.empty_cell_sym if not v else v
                row_html_string = row_html_string + "<td>{}</td>".format(v)
            row_html_string = row_html_string + "</tr>"
        return row_html_string

    @staticmethod
    def make_html_hyper_link(link, text):
        return '<a href="{}">{}</a>'.format(link, text)
