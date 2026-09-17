# DB2ADMIN.FINCSFI1

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `REPID`
- **FK degree**: referenced by 3 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103619

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REPID` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 1 | `REPORDER` | DECIMAL(2,0) |  |  |  |  |
| 2 | `REPNAME` | VARCHAR(100) |  |  |  |  |
| 3 | `REPPHP` | VARCHAR(100) |  |  |  |  |
| 4 | `REPIMAGE` | VARCHAR(100) |  |  |  |  |
| 5 | `REPMOBILE` | INTEGER | NOT NULL |  |  |  |
| 6 | `REPCLIENT` | INTEGER | NOT NULL |  |  |  |
| 7 | `REPBUT` | INTEGER | NOT NULL |  |  |  |
| 8 | `REPCHART` | INTEGER | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINCSFI1_RCFID` | [`FINCSFI2`](../FINANCE/FINCSFI2.md) | `RCFIDREPID` | `FINCSFI2.RCFIDREPID = FINCSFI1.REPID` |
| `FINCSFI1_RPTID2` | [`FINCSFI4`](../FINANCE/FINCSFI4.md) | `RPTID2REPID` | `FINCSFI4.RPTID2REPID = FINCSFI1.REPID` |
| `FINCSFI1_URSVREP` | [`FINCSFI7`](../FINANCE/FINCSFI7.md) | `URSVREPREPID` | `FINCSFI7.URSVREPREPID = FINCSFI1.REPID` |

## Indexes

- `FINCSFI1UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.REPID,
       t.REPORDER,
       t.REPNAME,
       t.REPPHP,
       t.REPIMAGE,
       t.REPMOBILE,
       t.REPCLIENT,
       t.REPBUT,
       t.REPCHART,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.FINCSFI1 t
FETCH FIRST 100 ROWS ONLY;
```
