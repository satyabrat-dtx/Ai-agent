# DB2ADMIN.BOMITEMSUBCODETEMPLATE

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`, `POSITION`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10569

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `POSITION` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `LENGTH` | INTEGER | NOT NULL |  |  |  |
| 4 | `TYPE` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `MANDATORY` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DATATYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `CHECKCODE` | CHAR(2) |  | FK | foreign_key |  |
| 8 | `GROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 9 | `OUTPUTSEPARATOR` | CHAR(2) |  |  |  |  |
| 10 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 11 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 12 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 13 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 15 | `DISTRIBUTIONCODE` | CHAR(30) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BOMITEMSUBCODETEMPLATE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMSUBCODECHECKTYPE_CHECK` | `CHECKCODE` | [`ITEMSUBCODECHECKTYPE`](../ITEM_MASTER/ITEMSUBCODECHECKTYPE.md) | `CODE` | RESTRICT | `BOMITEMSUBCODETEMPLATE.CHECKCODE = ITEMSUBCODECHECKTYPE.CODE` |
| `ITEMTYPE_BOMITEMSUBCODETEMPLATE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMITEMSUBCODETEMPLATE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND BOMITEMSUBCODETEMPLATE.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMITEMSUBCODETEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.POSITION,
       t.LENGTH,
       t.TYPE,
       t.MANDATORY,
       t.DATATYPE,
       t.CHECKCODE,
       t.GROUPTYPECODE,
       t.OUTPUTSEPARATOR,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION
FROM   DB2ADMIN.BOMITEMSUBCODETEMPLATE t
FETCH FIRST 100 ROWS ONLY;
```
