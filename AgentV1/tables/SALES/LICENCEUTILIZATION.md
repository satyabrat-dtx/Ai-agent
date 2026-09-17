# DB2ADMIN.LICENCEUTILIZATION

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 7 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140065

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `MRNHEADERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `MRNHEADERDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 5 | `MRNHEADERMRNPREFIXCODE` | CHAR(3) |  |  |  |  |
| 6 | `MRNHEADERCODE` | DECIMAL(11,0) |  |  |  |  |
| 7 | `SCHEMETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `ALCODE` | CHAR(30) |  | FK | foreign_key |  |
| 9 | `EGEPCGAPPLICATIONCODE` | CHAR(30) |  | FK | foreign_key |  |
| 10 | `DECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `DEDIVISIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `DECODE` | CHAR(12) |  | FK | foreign_key |  |
| 13 | `DBCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `DBDIVISIONCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `DBCODE` | CHAR(12) |  | FK | foreign_key |  |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 7

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ADVANCELICENSE_AL` | `COMPANYCODE`, `ALCODE` | [`ADVANCELICENSE`](../SALES/ADVANCELICENSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LICENCEUTILIZATION.COMPANYCODE = ADVANCELICENSE.COMPANYCODE AND LICENCEUTILIZATION.ALCODE = ADVANCELICENSE.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LICENCEUTILIZATION.COMPANYCODE = COMPANY.CODE` |
| `DBKAPPLICATION_DB` | `DBCOMPANYCODE`, `DBDIVISIONCODE`, `DBCODE` | [`DBKAPPLICATION`](../ITEM_MASTER/DBKAPPLICATION.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `LICENCEUTILIZATION.DBCOMPANYCODE = DBKAPPLICATION.COMPANYCODE AND LICENCEUTILIZATION.DBDIVISIONCODE = DBKAPPLICATION.DIVISIONCODE AND LICENCEUTILIZATION.DBCODE = DBKAPPLICATION.CODE` |
| `DEPBAPPLICATION_DE` | `DECOMPANYCODE`, `DEDIVISIONCODE`, `DECODE` | [`DEPBAPPLICATION`](../ITEM_MASTER/DEPBAPPLICATION.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `LICENCEUTILIZATION.DECOMPANYCODE = DEPBAPPLICATION.COMPANYCODE AND LICENCEUTILIZATION.DEDIVISIONCODE = DEPBAPPLICATION.DIVISIONCODE AND LICENCEUTILIZATION.DECODE = DEPBAPPLICATION.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LICENCEUTILIZATION.COMPANYCODE = DIVISION.COMPANYCODE AND LICENCEUTILIZATION.DIVISIONCODE = DIVISION.CODE` |
| `EPCGAPPLICATION_EGEPCGAPPLICATION` | `COMPANYCODE`, `EGEPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LICENCEUTILIZATION.COMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND LICENCEUTILIZATION.EGEPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LICENCEUTILIZATION.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND LICENCEUTILIZATION.SCHEMETYPECODE = SCHEMETYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LICENCEUTILIZATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.LINENO,
       t.MRNHEADERCOMPANYCODE,
       t.MRNHEADERDIVISIONCODE,
       t.MRNHEADERMRNPREFIXCODE,
       t.MRNHEADERCODE,
       t.SCHEMETYPECODE,
       t.ALCODE,
       t.EGEPCGAPPLICATIONCODE,
       t.DECOMPANYCODE,
       t.DEDIVISIONCODE
FROM   DB2ADMIN.LICENCEUTILIZATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
