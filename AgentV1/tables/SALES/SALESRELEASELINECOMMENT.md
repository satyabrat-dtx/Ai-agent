# DB2ADMIN.SALESRELEASELINECOMMENT

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `SALESRELEASELINECOMPANYCODE`, `SALESRELEASELINECODE`, `SALESRELEASELINELINE`, `SALESRELEASELINESUBLINE`, `SALRELEASELINECMPRELEASELINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24305

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `SALESRELEASELINECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `SALESRELEASELINECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `SALESRELEASELINELINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SALESRELEASELINESUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SALRELEASELINECMPRELEASELINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 6 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESRELEASELINE_COMMENT` | `SALESRELEASELINECOMPANYCODE`, `SALESRELEASELINECODE`, `SALESRELEASELINELINE`, `SALESRELEASELINESUBLINE`, `SALRELEASELINECMPRELEASELINE` | [`SALESRELEASELINE`](../SALES/SALESRELEASELINE.md) | `COMPANYCODE`, `CODE`, `LINE`, `SUBLINE`, `COMPONENTRELEASELINE` | RESTRICT | `SALESRELEASELINECOMMENT.SALESRELEASELINECOMPANYCODE = SALESRELEASELINE.COMPANYCODE AND SALESRELEASELINECOMMENT.SALESRELEASELINECODE = SALESRELEASELINE.CODE AND SALESRELEASELINECOMMENT.SALESRELEASELINELINE = SALESRELEASELINE.LINE AND SALESRELEASELINECOMMENT.SALESRELEASELINESUBLINE = SALESRELEASELINE.SUBLINE AND SALESRELEASELINECOMMENT.SALRELEASELINECMPRELEASELINE = SALESRELEASELINE.COMPONENTRELEASELINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESRELEASELINECOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.SALESRELEASELINECOMPANYCODE,
       t.SALESRELEASELINECODE,
       t.SALESRELEASELINELINE,
       t.SALESRELEASELINESUBLINE,
       t.SALRELEASELINECMPRELEASELINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.SALESRELEASELINECOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
