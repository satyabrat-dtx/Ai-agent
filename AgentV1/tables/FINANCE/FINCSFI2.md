# DB2ADMIN.FINCSFI2

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `RCFCONFID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103662

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `RCFCONFID` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `RCFIDREPID` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `RCFFNAME` | VARCHAR(100) |  |  |  |  |
| 3 | `RCFFTYPE` | VARCHAR(100) |  |  |  |  |
| 4 | `RCFFLEN` | DECIMAL(3,0) |  |  |  |  |
| 5 | `RCFVALUE` | VARCHAR(100) |  |  |  |  |
| 6 | `RCFDEFAULT` | VARCHAR(100) |  |  |  |  |
| 7 | `RCFHIDDEN` | INTEGER | NOT NULL |  |  |  |
| 8 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 9 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 10 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 11 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINCSFI1_RCFID` | `RCFIDREPID` | [`FINCSFI1`](../FINANCE/FINCSFI1.md) | `REPID` | RESTRICT | `FINCSFI2.RCFIDREPID = FINCSFI1.REPID` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINCSFI2UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.RCFCONFID,
       t.RCFIDREPID,
       t.RCFFNAME,
       t.RCFFTYPE,
       t.RCFFLEN,
       t.RCFVALUE,
       t.RCFDEFAULT,
       t.RCFHIDDEN,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER
FROM   DB2ADMIN.FINCSFI2 t
FETCH FIRST 100 ROWS ONLY;
```
