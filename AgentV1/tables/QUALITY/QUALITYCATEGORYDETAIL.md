# DB2ADMIN.QUALITYCATEGORYDETAIL

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `QUALITYCATEGORYCOMPANYCODE`, `QUALITYCATEGORYCODE`, `ITEMTYPECODE`, `QUALITYLEVELCODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123275

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `QUALITYCATEGORYCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `QUALITYCATEGORYCODE` | CHAR(2) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `QUALITYLVLITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 5 | `QUALITYLEVELCODE` | DECIMAL(2,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `QUALITYCATEGORY_DETAIL` | `QUALITYCATEGORYCOMPANYCODE`, `QUALITYCATEGORYCODE` | [`QUALITYCATEGORY`](../QUALITY/QUALITYCATEGORY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYCATEGORYDETAIL.QUALITYCATEGORYCOMPANYCODE = QUALITYCATEGORY.COMPANYCODE AND QUALITYCATEGORYDETAIL.QUALITYCATEGORYCODE = QUALITYCATEGORY.CODE` |
| `QUALITYLEVEL_QUALITYLEVEL` | `QUALITYLVLITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `QUALITYLEVELCODE` | [`QUALITYLEVEL`](../QUALITY/QUALITYLEVEL.md) | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `CODE` | RESTRICT | `QUALITYCATEGORYDETAIL.QUALITYLVLITEMTYPECOMPANYCODE = QUALITYLEVEL.ITEMTYPECOMPANYCODE AND QUALITYCATEGORYDETAIL.ITEMTYPECODE = QUALITYLEVEL.ITEMTYPECODE AND QUALITYCATEGORYDETAIL.QUALITYLEVELCODE = QUALITYLEVEL.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYCATEGORYDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.QUALITYCATEGORYCOMPANYCODE,
       t.QUALITYCATEGORYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.QUALITYLVLITEMTYPECOMPANYCODE,
       t.QUALITYLEVELCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.QUALITYCATEGORYDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
