# DB2ADMIN.REPLENISHMENTREQUISITIONCMT

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `REQREPCMYCODE`, `REQREPTMPCODE`, `REQREPCODE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 119879

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `REQREPCMYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `REQREPTMPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `REQREPCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 4 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 7 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 10 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 11 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 12 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 13 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 14 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 15 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `REPLENISHMENTREQUISITION_COMMENT` | `REQREPCMYCODE`, `REQREPTMPCODE`, `REQREPCODE` | [`REPLENISHMENTREQUISITION`](../PURCHASING/REPLENISHMENTREQUISITION.md) | `COMPANYCODE`, `REQUISITIONTEMPLATECODE`, `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONCMT.REQREPCMYCODE = REPLENISHMENTREQUISITION.COMPANYCODE AND REPLENISHMENTREQUISITIONCMT.REQREPTMPCODE = REPLENISHMENTREQUISITION.REQUISITIONTEMPLATECODE AND REPLENISHMENTREQUISITIONCMT.REQREPCODE = REPLENISHMENTREQUISITION.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LENISHMENTREQUISITIONCMTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.REQREPCMYCODE,
       t.REQREPTMPCODE,
       t.REQREPCODE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID,
       t.CREATIONDATETIME,
       t.CREATIONUSER
FROM   DB2ADMIN.REPLENISHMENTREQUISITIONCMT t
FETCH FIRST 100 ROWS ONLY;
```
