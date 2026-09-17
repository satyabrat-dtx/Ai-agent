# DB2ADMIN.FOCUSPRODUCTMASTERDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `FOCUSPRODUCTMASTERTARIFFCODE`, `FOCUSPRODUCTMASTERFOCUSSCHEME`, `FOCUSPRDMEFFECTIVEFROMDATE`, `COUNTRYCODE`, `EFFECTIVEFROMDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139286

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FOCUSPRODUCTMASTERTARIFFCODE` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FOCUSPRODUCTMASTERFOCUSSCHEME` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `FOCUSPRDMEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COUNTRYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `RATE` | DECIMAL(18,5) |  |  |  |  |
| 5 | `EFFECTIVEFROMDATE` | DATE | NOT NULL | PK | primary_key |  |
| 6 | `EFFECTIVETODATE` | DATE |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FOCUSPRODUCTMASTER_DETAIL` | `FOCUSPRODUCTMASTERTARIFFCODE`, `FOCUSPRODUCTMASTERFOCUSSCHEME`, `FOCUSPRDMEFFECTIVEFROMDATE` | [`FOCUSPRODUCTMASTER`](../OTHER/FOCUSPRODUCTMASTER.md) | `TARIFFCODE`, `FOCUSSCHEME`, `EFFECTIVEFROMDATE` | RESTRICT | `FOCUSPRODUCTMASTERDETAIL.FOCUSPRODUCTMASTERTARIFFCODE = FOCUSPRODUCTMASTER.TARIFFCODE AND FOCUSPRODUCTMASTERDETAIL.FOCUSPRODUCTMASTERFOCUSSCHEME = FOCUSPRODUCTMASTER.FOCUSSCHEME AND FOCUSPRODUCTMASTERDETAIL.FOCUSPRDMEFFECTIVEFROMDATE = FOCUSPRODUCTMASTER.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FOCUSPRODUCTMASTERDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FOCUSPRODUCTMASTERTARIFFCODE,
       t.FOCUSPRODUCTMASTERFOCUSSCHEME,
       t.FOCUSPRDMEFFECTIVEFROMDATE,
       t.COUNTRYCODE,
       t.RATE,
       t.EFFECTIVEFROMDATE,
       t.EFFECTIVETODATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.FOCUSPRODUCTMASTERDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
