# DB2ADMIN.FINMOTORPREMIUMCHARTDETAIL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 48
- **Primary key**: `FINMOTORPREMIUMCHARTCMYCODE`, `FINMOTORPREMIUMCHARTVEHICLETE`, `FINMOTORPREMIUMCHARTFROMDATE`, `AGEOFVEHICLE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230928

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINMOTORPREMIUMCHARTCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINMOTORPREMIUMCHARTVEHICLETE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FINMOTORPREMIUMCHARTFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `AGEOFVEHICLE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `TWSLAB1` | DECIMAL(18,5) |  |  |  |  |
| 5 | `TWSLAB2` | DECIMAL(18,5) |  |  |  |  |
| 6 | `TWSLAB3` | DECIMAL(18,5) |  |  |  |  |
| 7 | `TWSLAB4` | DECIMAL(18,5) |  |  |  |  |
| 8 | `TW1TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `TW2TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 10 | `TW3TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 11 | `TW4TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 12 | `TW1TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 13 | `TW2TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 14 | `TW3TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 15 | `TW4TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 16 | `PCSLAB1` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 17 | `PCSLAB2` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 18 | `PCSLAB3` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 19 | `PC1TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 20 | `PC2TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 21 | `PC3TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 22 | `PC1TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 23 | `PC2TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 24 | `PC3TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 25 | `PVSLAB1` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 26 | `PVSLAB1AP` | DECIMAL(18,5) |  |  |  |  |
| 27 | `PV1TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 28 | `PV1TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 29 | `PVSLAB2` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 30 | `PVSLAB2AP` | DECIMAL(18,5) |  |  |  |  |
| 31 | `PV2TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 32 | `PV2TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 33 | `PVSLAB3` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 34 | `PVSLAB3AP` | DECIMAL(18,5) |  |  |  |  |
| 35 | `PV3TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 36 | `PV3TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 37 | `PVSLAB4` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 38 | `PVSLAB4AP` | DECIMAL(18,5) |  |  |  |  |
| 39 | `PV4TPPREMIUMPERSONS` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 40 | `PV4TPPREMIUMVEHICLE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 41 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 42 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 43 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 44 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 45 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 46 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 47 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINMOTORPREMIUMCHART_LINE` | `FINMOTORPREMIUMCHARTCMYCODE`, `FINMOTORPREMIUMCHARTVEHICLETE`, `FINMOTORPREMIUMCHARTFROMDATE` | [`FINMOTORPREMIUMCHART`](../FINANCE/FINMOTORPREMIUMCHART.md) | `COMPANYCODE`, `VEHICLETYPE`, `FROMDATE` | RESTRICT | `FINMOTORPREMIUMCHARTDETAIL.FINMOTORPREMIUMCHARTCMYCODE = FINMOTORPREMIUMCHART.COMPANYCODE AND FINMOTORPREMIUMCHARTDETAIL.FINMOTORPREMIUMCHARTVEHICLETE = FINMOTORPREMIUMCHART.VEHICLETYPE AND FINMOTORPREMIUMCHARTDETAIL.FINMOTORPREMIUMCHARTFROMDATE = FINMOTORPREMIUMCHART.FROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINMOTORPREMIUMCHARTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINMOTORPREMIUMCHARTCMYCODE,
       t.FINMOTORPREMIUMCHARTVEHICLETE,
       t.FINMOTORPREMIUMCHARTFROMDATE,
       t.AGEOFVEHICLE,
       t.TWSLAB1,
       t.TWSLAB2,
       t.TWSLAB3,
       t.TWSLAB4,
       t.TW1TPPREMIUMPERSONS,
       t.TW2TPPREMIUMPERSONS,
       t.TW3TPPREMIUMPERSONS,
       t.TW4TPPREMIUMPERSONS
FROM   DB2ADMIN.FINMOTORPREMIUMCHARTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
