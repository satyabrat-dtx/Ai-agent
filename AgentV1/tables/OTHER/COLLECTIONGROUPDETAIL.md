# DB2ADMIN.COLLECTIONGROUPDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COLLECTIONGROUPCOMPANYCODE`, `COLLECTIONGROUPCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 16352

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COLLECTIONGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `COLLECTIONGROUPCODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COLLECTIONGROUP_DETAIL` | `COLLECTIONGROUPCOMPANYCODE`, `COLLECTIONGROUPCODE` | [`COLLECTIONGROUP`](../CORE_MASTER/COLLECTIONGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COLLECTIONGROUPDETAIL.COLLECTIONGROUPCOMPANYCODE = COLLECTIONGROUP.COMPANYCODE AND COLLECTIONGROUPDETAIL.COLLECTIONGROUPCODE = COLLECTIONGROUP.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `COLLECTIONGROUPDETAIL.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND COLLECTIONGROUPDETAIL.ITEMTYPEAFICODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COLLECTIONGROUPDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COLLECTIONGROUPCOMPANYCODE,
       t.COLLECTIONGROUPCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.COLLECTIONGROUPDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
