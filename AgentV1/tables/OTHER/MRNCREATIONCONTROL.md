# DB2ADMIN.MRNCREATIONCONTROL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `MRNPREFIXCODE`, `LOGICALWAREHOUSECODE`, `ITEMTYPECODE`, `FAGSTDORDERGROUPTYPEORDERTYPE`, `FAGSTANDARDORDERGROUPTYPECODE`, `FAGCODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 132931

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
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
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MRNCREATIONCONTROL.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MRNCREATIONCONTROL.COMPANYCODE = DIVISION.COMPANYCODE AND MRNCREATIONCONTROL.DIVISIONCODE = DIVISION.CODE` |
| `MRNPREFIX_MRNPREFIX` | `COMPANYCODE`, `DIVISIONCODE`, `MRNPREFIXCODE` | [`MRNPREFIX`](../OTHER/MRNPREFIX.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `MRNCREATIONCONTROL.COMPANYCODE = MRNPREFIX.COMPANYCODE AND MRNCREATIONCONTROL.DIVISIONCODE = MRNPREFIX.DIVISIONCODE AND MRNCREATIONCONTROL.MRNPREFIXCODE = MRNPREFIX.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MRNCREATIONCONTROLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.MRNPREFIXCODE,
       t.LOGICALWAREHOUSECOMPANYCODE,
       t.LOGICALWAREHOUSECODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.FAGSTDORDERGROUPTYPEORDERTYPE,
       t.FAGSTANDARDORDERGROUPTYPECODE,
       t.FAGCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.MRNCREATIONCONTROL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
