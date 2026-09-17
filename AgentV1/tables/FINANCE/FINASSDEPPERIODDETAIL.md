# DB2ADMIN.FINASSDEPPERIODDETAIL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 32
- **Primary key**: `FINASSDEPPERIODCOMPANYCODE`, `FINASSDEPPERIODDEPPERIODCODE`, `LINENUMBER`, `CREATIONTIMESTAMP`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 230614

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINASSDEPPERIODCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINASSDEPPERIODDEPPERIODCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENUMBER` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 3 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 4 | `BUSINESSUNITGROUP` | CHAR(10) |  |  |  |  |
| 5 | `BUSINESSUNIT` | CHAR(10) |  |  |  |  |
| 6 | `MAINASSET` | CHAR(15) |  |  |  |  |
| 7 | `ASSETNUMBER` | CHAR(15) |  |  |  |  |
| 8 | `ASSETDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `ACQUISVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ACCMDEPRECIATION` | DECIMAL(18,5) |  |  |  |  |
| 11 | `BOOKVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `DEPFORTHECURRENTPERIOD` | DECIMAL(18,5) |  |  |  |  |
| 13 | `COSTCENTER` | CHAR(20) |  |  |  |  |
| 14 | `PROFITCENTER` | CHAR(10) |  |  |  |  |
| 15 | `CURRENCY` | CHAR(4) |  |  |  |  |
| 16 | `ADDITIONALDEP` | CHAR(2) |  |  |  |  |
| 17 | `ASSETDEBITGLCODE` | CHAR(20) |  |  |  |  |
| 18 | `DOUBLESHIFTDAYS` | DECIMAL(5,2) |  |  |  |  |
| 19 | `THRIPLESHIFTDAYS` | DECIMAL(5,2) |  |  |  |  |
| 20 | `ASSETCREDITGLCODE` | CHAR(20) |  |  |  |  |
| 21 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 22 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 23 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 24 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 25 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 29 | `DEPFORTHE1SHIFT` | DECIMAL(18,5) |  |  |  |  |
| 30 | `DEPFORTHE2SHIFT` | DECIMAL(18,5) |  |  |  |  |
| 31 | `DEPFORTHE3SHIFT` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINASSETSDEPRECIATIONPERIOD_DETAIL` | `FINASSDEPPERIODCOMPANYCODE`, `FINASSDEPPERIODDEPPERIODCODE` | [`FINASSETSDEPRECIATIONPERIOD`](../FINANCE/FINASSETSDEPRECIATIONPERIOD.md) | `COMPANYCODE`, `DEPPERIODCODE` | RESTRICT | `FINASSDEPPERIODDETAIL.FINASSDEPPERIODCOMPANYCODE = FINASSETSDEPRECIATIONPERIOD.COMPANYCODE AND FINASSDEPPERIODDETAIL.FINASSDEPPERIODDEPPERIODCODE = FINASSETSDEPRECIATIONPERIOD.DEPPERIODCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINASSDEPPERIODDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINASSDEPPERIODCOMPANYCODE,
       t.FINASSDEPPERIODDEPPERIODCODE,
       t.LINENUMBER,
       t.CREATIONTIMESTAMP,
       t.BUSINESSUNITGROUP,
       t.BUSINESSUNIT,
       t.MAINASSET,
       t.ASSETNUMBER,
       t.ASSETDESCRIPTION,
       t.ACQUISVALUE,
       t.ACCMDEPRECIATION,
       t.BOOKVALUE
FROM   DB2ADMIN.FINASSDEPPERIODDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
