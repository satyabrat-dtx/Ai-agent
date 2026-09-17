# DB2ADMIN.FINCSFI4

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `RPTID2REPID`, `RPTLNG`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103742

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RPTID2REPID` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `RPTLNG` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 2 | `RPTTXT` | VARCHAR(100) |  |  |  |  |
| 3 | `RPTTXT2` | VARCHAR(255) |  |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINCSFI1_RPTID2` | `RPTID2REPID` | [`FINCSFI1`](../FINANCE/FINCSFI1.md) | `REPID` | RESTRICT | `FINCSFI4.RPTID2REPID = FINCSFI1.REPID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCSFI4UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RPTID2REPID,
       t.RPTLNG,
       t.RPTTXT,
       t.RPTTXT2,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINCSFI4 t
FETCH FIRST 100 ROWS ONLY;
```
