# DB2ADMIN.EXTOPLINEPRODUCTIONPROGRESS

- **Module**: `SUBCONTRACTING` (medium confidence — table name starts with 'EXTOP')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `EOLCOMPANYCODE`, `EOLCOUNTERCODE`, `EOLCODE`, `EOLLINE`, `PROGRESSNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 197784

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EOLCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EOLCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `EOLCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `EOLLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PROGRESSNUMBER` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PROGRESSDELETED` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ISQUEUEPROGRESS` | SMALLINT | NOT NULL |  |  |  |
| 7 | `EXTOPLINECANCELLED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `PDEDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `PDEDEMANDCODE` | CHAR(15) |  |  |  |  |
| 10 | `PDEITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 11 | `PDEELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 12 | `PDEELEMENTCODE` | CHAR(15) |  |  |  |  |
| 13 | `PRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PRIMARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `SECONDARYUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `PACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `PACKAGINGUOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `USEDPRIMARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `USEDSECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 21 | `USEDPACKAGINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  |  |  |  |
| 30 | `TERMSOFLOGCODE` | CHAR(2) |  |  |  |  |
| 31 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EXTOPLINE_PROGRESS` | `EOLCOMPANYCODE`, `EOLCOUNTERCODE`, `EOLCODE`, `EOLLINE` | [`EXTOPLINE`](../SUBCONTRACTING/EXTOPLINE.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE`, `ORDERLINE` | RESTRICT | `EXTOPLINEPRODUCTIONPROGRESS.EOLCOMPANYCODE = EXTOPLINE.COMPANYCODE AND EXTOPLINEPRODUCTIONPROGRESS.EOLCOUNTERCODE = EXTOPLINE.COUNTERCODE AND EXTOPLINEPRODUCTIONPROGRESS.EOLCODE = EXTOPLINE.CODE AND EXTOPLINEPRODUCTIONPROGRESS.EOLLINE = EXTOPLINE.ORDERLINE` |
| `LOGREASON_LOGREASON` | `EOLCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTOPLINEPRODUCTIONPROGRESS.EOLCOMPANYCODE = LOGREASON.COMPANYCODE AND EXTOPLINEPRODUCTIONPROGRESS.LOGREASONCODE = LOGREASON.CODE` |
| `PRODUCTIONPROGRESS_PRODUCTIONPROGRESS` | `EOLCOMPANYCODE`, `PROGRESSNUMBER` | [`PRODUCTIONPROGRESS`](../PRODUCTION/PRODUCTIONPROGRESS.md) | `COMPANYCODE`, `PROGRESSNUMBER` | RESTRICT | `EXTOPLINEPRODUCTIONPROGRESS.EOLCOMPANYCODE = PRODUCTIONPROGRESS.COMPANYCODE AND EXTOPLINEPRODUCTIONPROGRESS.PROGRESSNUMBER = PRODUCTIONPROGRESS.PROGRESSNUMBER` |
| `UNITOFMEASURE_PACKAGINGUOM` | `PACKAGINGUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `EXTOPLINEPRODUCTIONPROGRESS.PACKAGINGUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_PRIMARYUOM` | `PRIMARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `EXTOPLINEPRODUCTIONPROGRESS.PRIMARYUOMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SECONDARYUOM` | `SECONDARYUOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `EXTOPLINEPRODUCTIONPROGRESS.SECONDARYUOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTOPLINEPROPROGRESSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EOLCOMPANYCODE,
       t.EOLCOUNTERCODE,
       t.EOLCODE,
       t.EOLLINE,
       t.PROGRESSNUMBER,
       t.PROGRESSDELETED,
       t.ISQUEUEPROGRESS,
       t.EXTOPLINECANCELLED,
       t.PDEDEMANDCOUNTERCODE,
       t.PDEDEMANDCODE,
       t.PDEITEMTYPEAFICODE,
       t.PDEELEMENTSUBCODEKEY
FROM   DB2ADMIN.EXTOPLINEPRODUCTIONPROGRESS t
FETCH FIRST 100 ROWS ONLY;
```
