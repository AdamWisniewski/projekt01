# -*- coding: utf-8 -*-
import pymysql
from main import *


# polecenia testujące

connectDatabase()
a = Admin()
a.dispLegendAdmin()
a.dispAllProcedures()