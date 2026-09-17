# DB2ADMIN.INSTALLATION

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `EPCGAPPCAPGOODSEPCGAPPCMYCODE`, `EPCGAPPCAPGOODSEPCGAPPCODE`, `EPCGAPPCAPITALGOODSLINENO`, `PLANT1CODE`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139374

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EPCGAPPCAPGOODSEPCGAPPCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EPCGAPPCAPGOODSEPCGAPPCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EPCGAPPCAPITALGOODSLINENO` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINEID` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `INSTALLATIONCERTNEEDED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `INSTALLATIONDATE` | DATE |  |  |  |  |
| 6 | `ENDUSECERTIFICATE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `INSTALLATIONENDDATE` | DATE |  |  |  |  |
| 8 | `NOOFMACHINES` | INTEGER | NOT NULL |  |  |  |
| 9 | `PLANT1COMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 10 | `PLANT1CODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 11 | `REMARK1` | CHAR(50) |  |  |  |  |
| 12 | `REMARK2` | CHAR(50) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EPCGAPPLICATIONCAPITALGOODS_INSTALLATION` | `EPCGAPPCAPGOODSEPCGAPPCMYCODE`, `EPCGAPPCAPGOODSEPCGAPPCODE`, `EPCGAPPCAPITALGOODSLINENO` | [`EPCGAPPLICATIONCAPITALGOODS`](../PURCHASING/EPCGAPPLICATIONCAPITALGOODS.md) | `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE`, `LINENO` | RESTRICT | `INSTALLATION.EPCGAPPCAPGOODSEPCGAPPCMYCODE = EPCGAPPLICATIONCAPITALGOODS.EPCGAPPLICATIONCOMPANYCODE AND INSTALLATION.EPCGAPPCAPGOODSEPCGAPPCODE = EPCGAPPLICATIONCAPITALGOODS.EPCGAPPLICATIONCODE AND INSTALLATION.EPCGAPPCAPITALGOODSLINENO = EPCGAPPLICATIONCAPITALGOODS.LINENO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `INSTALLATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EPCGAPPCAPGOODSEPCGAPPCMYCODE,
       t.EPCGAPPCAPGOODSEPCGAPPCODE,
       t.EPCGAPPCAPITALGOODSLINENO,
       t.LINEID,
       t.INSTALLATIONCERTNEEDED,
       t.INSTALLATIONDATE,
       t.ENDUSECERTIFICATE,
       t.INSTALLATIONENDDATE,
       t.NOOFMACHINES,
       t.PLANT1COMPANYCODE,
       t.PLANT1CODE,
       t.REMARK1
FROM   DB2ADMIN.INSTALLATION t
FETCH FIRST 100 ROWS ONLY;
```
