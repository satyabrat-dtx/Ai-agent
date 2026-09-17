# DB2ADMIN.DESIGNENGINEERINGCHANGELOG

- **Module**: `LOGISTICS` (low confidence — FK neighbourhood: 1 of 1 related tables are LOGISTICS)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `DESIGNCOMPANYCODE`, `DESIGNNUMBERID`, `ENGINEERINGCHANGENUMBERID`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 7541

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DESIGNCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DESIGNNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ENGINEERINGCHANGENUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `LOGREASONCODE` | CHAR(2) |  | FK | foreign_key |  |
| 6 | `DESIGNITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `DESIGNSUBCODE01` | CHAR(20) | NOT NULL |  |  |  |
| 8 | `DESIGNSUBCODE02` | CHAR(10) |  |  |  |  |
| 9 | `DESIGNSUBCODE03` | CHAR(10) |  |  |  |  |
| 10 | `DESIGNSUBCODE04` | CHAR(10) |  |  |  |  |
| 11 | `DESIGNSUBCODE05` | CHAR(10) |  |  |  |  |
| 12 | `DESIGNSUBCODE06` | CHAR(10) |  |  |  |  |
| 13 | `DESIGNSUBCODE07` | CHAR(10) |  |  |  |  |
| 14 | `DESIGNSUBCODE08` | CHAR(10) |  |  |  |  |
| 15 | `DESIGNSUBCODE09` | CHAR(10) |  |  |  |  |
| 16 | `DESIGNSUBCODE10` | CHAR(10) |  |  |  |  |
| 17 | `DESIGNSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 18 | `RELEASEDATE` | DATE |  |  |  |  |
| 19 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 20 | `APPLICABLE` | SMALLINT | NOT NULL |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 26 | `DESIGNITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 29 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNENGINEERINGCHANGELOG.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND DESIGNENGINEERINGCHANGELOG.COUNTERCODE = COUNTER.CODE` |
| `DESIGN_ENGINEERINGCHANGELOG` | `DESIGNCOMPANYCODE`, `DESIGNNUMBERID` | [`DESIGN`](../PRODUCTION/DESIGN.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `DESIGNENGINEERINGCHANGELOG.DESIGNCOMPANYCODE = DESIGN.COMPANYCODE AND DESIGNENGINEERINGCHANGELOG.DESIGNNUMBERID = DESIGN.NUMBERID` |
| `ENGINEERINGCHANGE_ENGINEERINGCHANGE` | `DESIGNCOMPANYCODE`, `ENGINEERINGCHANGENUMBERID` | [`ENGINEERINGCHANGE`](../CORE_MASTER/ENGINEERINGCHANGE.md) | `COMPANYCODE`, `NUMBERID` | RESTRICT | `DESIGNENGINEERINGCHANGELOG.DESIGNCOMPANYCODE = ENGINEERINGCHANGE.COMPANYCODE AND DESIGNENGINEERINGCHANGELOG.ENGINEERINGCHANGENUMBERID = ENGINEERINGCHANGE.NUMBERID` |
| `ITEMTYPE_DESIGNITEMTYPE` | `DESIGNITEMTYPECOMPANYCODE`, `DESIGNITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNENGINEERINGCHANGELOG.DESIGNITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND DESIGNENGINEERINGCHANGELOG.DESIGNITEMTYPECODE = ITEMTYPE.CODE` |
| `LOGREASON_LOGREASON` | `DESIGNCOMPANYCODE`, `LOGREASONCODE` | [`LOGREASON`](../LOGISTICS/LOGREASON.md) | `COMPANYCODE`, `CODE` | RESTRICT | `DESIGNENGINEERINGCHANGELOG.DESIGNCOMPANYCODE = LOGREASON.COMPANYCODE AND DESIGNENGINEERINGCHANGELOG.LOGREASONCODE = LOGREASON.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DESIGNENGINEERINGCHANGELOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DESIGNCOMPANYCODE,
       t.DESIGNNUMBERID,
       t.ENGINEERINGCHANGENUMBERID,
       t.COUNTERCODE,
       t.CODE,
       t.LOGREASONCODE,
       t.DESIGNITEMTYPECODE,
       t.DESIGNSUBCODE01,
       t.DESIGNSUBCODE02,
       t.DESIGNSUBCODE03,
       t.DESIGNSUBCODE04,
       t.DESIGNSUBCODE05
FROM   DB2ADMIN.DESIGNENGINEERINGCHANGELOG t
FETCH FIRST 100 ROWS ONLY;
```
