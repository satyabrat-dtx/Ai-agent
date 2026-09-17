# DB2ADMIN.ALLOWEDFORITEMTYPE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 206437

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ALLOWEDITEMTYPENOTEKEY` | VARCHAR(250) |  |  |  |  |
| 3 | `ALLOWEDITEMTYPENOTEMANDATORY` | VARCHAR(250) |  |  |  |  |
| 4 | `ALLOWEDITEMTYPENOTEHIGHLIGHT` | VARCHAR(250) |  |  |  |  |
| 5 | `ALWITEMTYPECOMPONENTGROUPKEY` | VARCHAR(250) |  |  |  |  |
| 6 | `ALLOWEDITEMTYPESKETCHGROUPKEY` | VARCHAR(250) |  |  |  |  |
| 7 | `ALWITEMTYPESKETCHTYPEDLTKEY` | VARCHAR(250) |  |  |  |  |
| 8 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ALLOWEDFORITEMTYPE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ALLOWEDFORITEMTYPE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ALLOWEDFORITEMTYPE.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ALLOWEDFORITEMTYPEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ALLOWEDITEMTYPENOTEKEY,
       t.ALLOWEDITEMTYPENOTEMANDATORY,
       t.ALLOWEDITEMTYPENOTEHIGHLIGHT,
       t.ALWITEMTYPECOMPONENTGROUPKEY,
       t.ALLOWEDITEMTYPESKETCHGROUPKEY,
       t.ALWITEMTYPESKETCHTYPEDLTKEY,
       t.OWNINGCOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ALLOWEDFORITEMTYPE t
FETCH FIRST 100 ROWS ONLY;
```
