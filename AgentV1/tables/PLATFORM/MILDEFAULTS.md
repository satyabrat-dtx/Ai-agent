# DB2ADMIN.MILDEFAULTS

- **Module**: `PLATFORM` (low confidence — FK neighbourhood: 1 of 1 related tables are PLATFORM)
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 33679

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 2 | `COUNTERCODE` | CHAR(8) |  |  |  |  |
| 3 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 4 | `LINETEMPLATECODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 6 | `TAXCODE` | CHAR(3) |  |  |  |  |
| 7 | `DEFAULTUSERUSERID` | CHAR(25) |  | FK | foreign_key |  |
| 8 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ABSUSERDEF_DEFAULTUSER` | `DEFAULTUSERUSERID` | [`ABSUSERDEF`](../PLATFORM/ABSUSERDEF.md) | `USERID` | RESTRICT | `MILDEFAULTS.DEFAULTUSERUSERID = ABSUSERDEF.USERID` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MILDEFAULTS.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MILDEFAULTS.COMPANYCODE = DIVISION.COMPANYCODE AND MILDEFAULTS.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MILDEFAULTS.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND MILDEFAULTS.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MILDEFAULTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.COUNTERCODE,
       t.TEMPLATECODE,
       t.LINETEMPLATECODE,
       t.DIVISIONCODE,
       t.TAXCODE,
       t.DEFAULTUSERUSERID,
       t.ITEMTYPECOMPANYCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.MILDEFAULTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
