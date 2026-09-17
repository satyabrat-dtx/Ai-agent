# DB2ADMIN.ARTICLESTATUSLOG

- **Module**: `TNA` (low confidence — FK neighbourhood: 1 of 1 related tables are TNA)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `UNIQUEID`, `LINENUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190012

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UNIQUEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `LINENUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(8) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `ACTION` | INTEGER | NOT NULL |  |  |  |
| 4 | `REASONCODECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `REASONCODEREASONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `REASONCOMMENT` | CHAR(100) |  |  |  |  |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `CHANGEDATETIME` | TIMESTAMP |  |  |  |  |
| 9 | `LOGTIMESTAMP` | BIGINT | NOT NULL |  | audit | When the audited change was recorded (change-log table). |
| 10 | `ENABLED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `STATUSREASON_REASONCODE` | `REASONCODECOMPANYCODE`, `REASONCODEREASONCODE` | [`STATUSREASON`](../TNA/STATUSREASON.md) | `COMPANYCODE`, `REASONCODE` | RESTRICT | `ARTICLESTATUSLOG.REASONCODECOMPANYCODE = STATUSREASON.COMPANYCODE AND ARTICLESTATUSLOG.REASONCODEREASONCODE = STATUSREASON.REASONCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ARTICLESTATUSLOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UNIQUEID,
       t.LINENUMBER,
       t.CODE,
       t.ACTION,
       t.REASONCODECOMPANYCODE,
       t.REASONCODEREASONCODE,
       t.REASONCOMMENT,
       t.CREATIONUSER,
       t.CHANGEDATETIME,
       t.LOGTIMESTAMP,
       t.ENABLED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ARTICLESTATUSLOG t
FETCH FIRST 100 ROWS ONLY;
```
