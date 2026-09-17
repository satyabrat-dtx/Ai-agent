# DB2ADMIN.USASTCONTROLDATE

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'USA')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE`, `ACCOUNTTYPE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108055

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `WHSACCOUNTINGGROUPCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `WAREHOUSEACCOUNTINGGROUPCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ACCOUNTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 4 | `INITIALDATE` | DATE |  |  |  |  |
| 5 | `LASTDATE` | DATE |  |  |  |  |
| 6 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `USASTCONTROLDATE.COMPANYCODE = COMPANY.CODE` |
| `WAREHOUSEACCOUNTINGGROUP_WAREHOUSEACCOUNTINGGROUP` | `WHSACCOUNTINGGROUPCOMPANYCODE`, `WAREHOUSEACCOUNTINGGROUPCODE` | [`WAREHOUSEACCOUNTINGGROUP`](../WAREHOUSE/WAREHOUSEACCOUNTINGGROUP.md) | `COMPANYCODE`, `CODE` | RESTRICT | `USASTCONTROLDATE.WHSACCOUNTINGGROUPCOMPANYCODE = WAREHOUSEACCOUNTINGGROUP.COMPANYCODE AND USASTCONTROLDATE.WAREHOUSEACCOUNTINGGROUPCODE = WAREHOUSEACCOUNTINGGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `USASTCONTROLDATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.WHSACCOUNTINGGROUPCOMPANYCODE,
       t.WAREHOUSEACCOUNTINGGROUPCODE,
       t.ACCOUNTTYPE,
       t.INITIALDATE,
       t.LASTDATE,
       t.PROGRESSSTATUS,
       t.ABSUNIQUEID
FROM   DB2ADMIN.USASTCONTROLDATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
