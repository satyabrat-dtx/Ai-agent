# DB2ADMIN.EXTERNALPRCLISTDEFCOMMENT

- **Module**: `SUBCONTRACTING` (low confidence — FK neighbourhood: 1 of 1 related tables are SUBCONTRACTING)
- **Roles**: `business_data`
- **Columns**: 15
- **Primary key**: `EXTOPPRICELISTCOMPANYCODE`, `EXTOPPRICELISTCODE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 39264

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EXTOPPRICELISTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EXTOPPRICELISTCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 3 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 6 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EXTOPPRICELIST_COMMENT` | `EXTOPPRICELISTCOMPANYCODE`, `EXTOPPRICELISTCODE` | [`EXTOPPRICELIST`](../SUBCONTRACTING/EXTOPPRICELIST.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EXTERNALPRCLISTDEFCOMMENT.EXTOPPRICELISTCOMPANYCODE = EXTOPPRICELIST.COMPANYCODE AND EXTERNALPRCLISTDEFCOMMENT.EXTOPPRICELISTCODE = EXTOPPRICELIST.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EXTERNALPRCLISTDEFCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EXTOPPRICELISTCOMPANYCODE,
       t.EXTOPPRICELISTCODE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.EXTERNALPRCLISTDEFCOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
