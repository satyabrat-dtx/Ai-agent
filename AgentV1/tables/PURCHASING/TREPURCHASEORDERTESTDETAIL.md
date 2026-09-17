# DB2ADMIN.TREPURCHASEORDERTESTDETAIL

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `TREPURORDTESTGROUPCOMPANYCODE`, `TREPURCHASEORDERTESTGROUPCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 69510

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TREPURORDTESTGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TREPURCHASEORDERTESTGROUPCODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(4) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `SEQUENCETEST` | DECIMAL(5,0) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TREPURCHASEORDERTESTGROUP_TESTDETAIL` | `TREPURORDTESTGROUPCOMPANYCODE`, `TREPURCHASEORDERTESTGROUPCODE` | [`TREPURCHASEORDERTESTGROUP`](../PURCHASING/TREPURCHASEORDERTESTGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `TREPURCHASEORDERTESTDETAIL.TREPURORDTESTGROUPCOMPANYCODE = TREPURCHASEORDERTESTGROUP.COMPANYCODE AND TREPURCHASEORDERTESTDETAIL.TREPURCHASEORDERTESTGROUPCODE = TREPURCHASEORDERTESTGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TREPURCHASEORDERTESTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TREPURORDTESTGROUPCOMPANYCODE,
       t.TREPURCHASEORDERTESTGROUPCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.SEQUENCETEST,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TREPURCHASEORDERTESTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
