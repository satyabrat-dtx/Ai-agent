# DB2ADMIN.FINEXPREALISATIONFCDETAIL

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `FINEXPREALISATIONCOMPANYCODE`, `FINEXPREALISATIONCODE`, `FORWARDCONTRACTFCNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227232

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPREALISATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINEXPREALISATIONCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FORWARDCONTRACTFCNO` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 3 | `FCVALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 4 | `FCRATE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `ADJUSTABLEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 6 | `UNUTILISED` | DECIMAL(18,5) |  |  |  |  |
| 7 | `UTILISED` | DECIMAL(18,5) |  |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 12 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 13 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINEXPREALISATION_FINEXPREALISATIONFCDETAIL` | `FINEXPREALISATIONCOMPANYCODE`, `FINEXPREALISATIONCODE` | [`FINEXPREALISATION`](../FINANCE/FINEXPREALISATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPREALISATIONFCDETAIL.FINEXPREALISATIONCOMPANYCODE = FINEXPREALISATION.COMPANYCODE AND FINEXPREALISATIONFCDETAIL.FINEXPREALISATIONCODE = FINEXPREALISATION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPREALISATIONFCDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINEXPREALISATIONCOMPANYCODE,
       t.FINEXPREALISATIONCODE,
       t.FORWARDCONTRACTFCNO,
       t.FCVALUE,
       t.FCRATE,
       t.ADJUSTABLEVALUE,
       t.UNUTILISED,
       t.UTILISED,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINEXPREALISATIONFCDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
