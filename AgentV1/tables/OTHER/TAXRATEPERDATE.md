# DB2ADMIN.TAXRATEPERDATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `TAXCOMPANYCODE`, `TAXCODE`, `INITIALDATE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 191803

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TAXCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TAXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `INITIALDATE` | DATE | NOT NULL | PK | primary_key |  |
| 3 | `RATE` | DECIMAL(6,3) |  |  |  |  |
| 4 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 5 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 6 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 7 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 8 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 9 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 10 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TAX_TAXVALIDITYDATE` | `TAXCOMPANYCODE`, `TAXCODE` | [`TAX`](../CORE_MASTER/TAX.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TAXRATEPERDATE.TAXCOMPANYCODE = TAX.COMPANYCODE AND TAXRATEPERDATE.TAXCODE = TAX.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TAXRATEPERDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TAXCOMPANYCODE,
       t.TAXCODE,
       t.INITIALDATE,
       t.RATE,
       t.EXPIRATIONDATE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TAXRATEPERDATE t
FETCH FIRST 100 ROWS ONLY;
```
