# DB2ADMIN.PLANTINVCREATIONCTRL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `INVOICETYPECODE`, `LOGICALWAREHOUSECODE`, `ITEMTYPECODE`, `FAGSTDORDERGROUPTYPEORDERTYPE`, `FAGSTANDARDORDERGROUPTYPECODE`, `FAGCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140988

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 7 | `FAGSTDORDERGROUPTYPEORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 8 | `FAGSTANDARDORDERGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 9 | `FAGCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PLANTINVCREATIONCTRL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLANTINVCREATIONCTRL.COMPANYCODE = DIVISION.COMPANYCODE AND PLANTINVCREATIONCTRL.DIVISIONCODE = DIVISION.CODE` |
| `INVOICETYPE_INVOICETYPE` | `COMPANYCODE`, `DIVISIONCODE`, `INVOICETYPECODE` | [`INVOICETYPE`](../SALES/INVOICETYPE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PLANTINVCREATIONCTRL.COMPANYCODE = INVOICETYPE.COMPANYCODE AND PLANTINVCREATIONCTRL.DIVISIONCODE = INVOICETYPE.DIVISIONCODE AND PLANTINVCREATIONCTRL.INVOICETYPECODE = INVOICETYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANTINVCREATIONCTRLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INVOICETYPECODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.FAGSTDORDERGROUPTYPEORDERTYPE,
       t.FAGSTANDARDORDERGROUPTYPECODE,
       t.FAGCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PLANTINVCREATIONCTRL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
