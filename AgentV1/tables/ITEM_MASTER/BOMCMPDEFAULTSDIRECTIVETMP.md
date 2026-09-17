# DB2ADMIN.BOMCMPDEFAULTSDIRECTIVETMP

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 12
- **Primary key**: `BCDCOMPANYCODE`, `BCDFATHERITEMTYPECODE`, `BCDCOMPITEMTYPECODE`, `DIRECTIVETEMPLATECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 198816

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BCDCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `BCDFATHERITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `BCDCOMPITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `DIRECTIVETEMPLATECODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `MATRIXTYPECODE` | CHAR(10) |  | FK | foreign_key |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BOMCOMPONENTDEFAULTS_DIRECTIVETEMPLATE` | `BCDCOMPANYCODE`, `BCDFATHERITEMTYPECODE`, `BCDCOMPITEMTYPECODE` | [`BOMCOMPONENTDEFAULTS`](../ITEM_MASTER/BOMCOMPONENTDEFAULTS.md) | `COMPANYCODE`, `FATHERITEMTYPECODE`, `COMPITEMTYPECODE` | RESTRICT | `BOMCMPDEFAULTSDIRECTIVETMP.BCDCOMPANYCODE = BOMCOMPONENTDEFAULTS.COMPANYCODE AND BOMCMPDEFAULTSDIRECTIVETMP.BCDFATHERITEMTYPECODE = BOMCOMPONENTDEFAULTS.FATHERITEMTYPECODE AND BOMCMPDEFAULTSDIRECTIVETMP.BCDCOMPITEMTYPECODE = BOMCOMPONENTDEFAULTS.COMPITEMTYPECODE` |
| `DIRECTIVETEMPLATE_DIRECTIVETEMPLATE` | `BCDCOMPANYCODE`, `DIRECTIVETEMPLATECODE` | [`DIRECTIVETEMPLATE`](../ITEM_MASTER/DIRECTIVETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMCMPDEFAULTSDIRECTIVETMP.BCDCOMPANYCODE = DIRECTIVETEMPLATE.COMPANYCODE AND BOMCMPDEFAULTSDIRECTIVETMP.DIRECTIVETEMPLATECODE = DIRECTIVETEMPLATE.CODE` |
| `MATRIXCATEGORY_MATRIXTYPE` | `BCDCOMPANYCODE`, `MATRIXTYPECODE` | [`MATRIXCATEGORY`](../ITEM_MASTER/MATRIXCATEGORY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMCMPDEFAULTSDIRECTIVETMP.BCDCOMPANYCODE = MATRIXCATEGORY.COMPANYCODE AND BOMCMPDEFAULTSDIRECTIVETMP.MATRIXTYPECODE = MATRIXCATEGORY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMCMPDEFAULTSDIRECTIVETMPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.BCDCOMPANYCODE,
       t.BCDFATHERITEMTYPECODE,
       t.BCDCOMPITEMTYPECODE,
       t.DIRECTIVETEMPLATECODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID,
       t.MATRIXTYPECODE
FROM   DB2ADMIN.BOMCMPDEFAULTSDIRECTIVETMP t
FETCH FIRST 100 ROWS ONLY;
```
