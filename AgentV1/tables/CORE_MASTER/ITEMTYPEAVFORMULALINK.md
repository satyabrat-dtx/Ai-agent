# DB2ADMIN.ITEMTYPEAVFORMULALINK

- **Module**: `CORE_MASTER` (high confidence — table name starts with 'ITEMTYPE')
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `USEDFOR`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 83010

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `AVAILABILITYFORMULACOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `AVAILABILITYFORMULACODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 6 | `USEDFOR` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `BALANCEFORMULACOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `BALANCEFORMULACODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `AVAILABILITYFORMULA_AVAILABILITYFORMULA` | `AVAILABILITYFORMULACOMPANYCODE`, `AVAILABILITYFORMULACODE` | [`AVAILABILITYFORMULA`](../CORE_MASTER/AVAILABILITYFORMULA.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMTYPEAVFORMULALINK.AVAILABILITYFORMULACOMPANYCODE = AVAILABILITYFORMULA.COMPANYCODE AND ITEMTYPEAVFORMULALINK.AVAILABILITYFORMULACODE = AVAILABILITYFORMULA.CODE` |
| `AVAILABILITYFORMULA_BALANCEFORMULA` | `BALANCEFORMULACOMPANYCODE`, `BALANCEFORMULACODE` | [`AVAILABILITYFORMULA`](../CORE_MASTER/AVAILABILITYFORMULA.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ITEMTYPEAVFORMULALINK.BALANCEFORMULACOMPANYCODE = AVAILABILITYFORMULA.COMPANYCODE AND ITEMTYPEAVFORMULALINK.BALANCEFORMULACODE = AVAILABILITYFORMULA.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ITEMTYPEAVFORMULALINK.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ITEMTYPEAVFORMULALINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.AVAILABILITYFORMULACOMPANYCODE,
       t.AVAILABILITYFORMULACODE,
       t.ABSUNIQUEID,
       t.USEDFOR,
       t.BALANCEFORMULACOMPANYCODE,
       t.BALANCEFORMULACODE
FROM   DB2ADMIN.ITEMTYPEAVFORMULALINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
