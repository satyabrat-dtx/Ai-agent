# DB2ADMIN.SALESORDERGROUPCOMMENT

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE`, `LINEGROUP`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18483

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `LINEGROUP` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 6 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 7 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 8 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 9 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESORDER_GROUPCOMMENT` | `SALESORDERCOMPANYCODE`, `SALESORDERCOUNTERCODE`, `SALESORDERCODE` | [`SALESORDER`](../SALES/SALESORDER.md) | `COMPANYCODE`, `COUNTERCODE`, `CODE` | RESTRICT | `SALESORDERGROUPCOMMENT.SALESORDERCOMPANYCODE = SALESORDER.COMPANYCODE AND SALESORDERGROUPCOMMENT.SALESORDERCOUNTERCODE = SALESORDER.COUNTERCODE AND SALESORDERGROUPCOMMENT.SALESORDERCODE = SALESORDER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERGROUPCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESORDERCOMPANYCODE,
       t.SALESORDERCOUNTERCODE,
       t.SALESORDERCODE,
       t.REPORTTYPE,
       t.LINEGROUP,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME
FROM   DB2ADMIN.SALESORDERGROUPCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
