# DB2ADMIN.MILSALORDCOMMENTIMP

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `MILSALORDIMPCC`, `MILSALORDIMPIC`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33776

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MILSALORDIMPCC` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MILSALORDIMPIC` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `IMPORTOPERATION` | INTEGER | NOT NULL |  |  |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 7 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `MILSALORDIMP_COMMENT` | `MILSALORDIMPCC`, `MILSALORDIMPIC` | [`MILSALORDIMP`](../SALES/MILSALORDIMP.md) | `CC`, `IC` | RESTRICT | `MILSALORDCOMMENTIMP.MILSALORDIMPCC = MILSALORDIMP.CC AND MILSALORDCOMMENTIMP.MILSALORDIMPIC = MILSALORDIMP.IC` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MILSALORDCOMMENTIMPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MILSALORDIMPCC,
       t.MILSALORDIMPIC,
       t.IMPORTOPERATION,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.MILSALORDCOMMENTIMP t
FETCH FIRST 100 ROWS ONLY;
```
