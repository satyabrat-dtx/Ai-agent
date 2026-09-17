# DB2ADMIN.ISDEPCGMAPPING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `INVOICETYPECODE`, `PORTCODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139333

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `INVOICETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PORTCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `EPCGAPPLICATIONCODE` | CHAR(30) |  | FK | foreign_key |  |
| 5 | `EPCGAPPLICATIONDATE` | DATE |  |  |  |  |
| 6 | `EPCGLICENSENO` | CHAR(30) |  |  |  |  |
| 7 | `EPCGLICENSEDATE` | DATE |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ISDEPCGMAPPING.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ISDEPCGMAPPING.COMPANYCODE = DIVISION.COMPANYCODE AND ISDEPCGMAPPING.DIVISIONCODE = DIVISION.CODE` |
| `EPCGAPPLICATION_EPCGAPPLICATION` | `COMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ISDEPCGMAPPING.COMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND ISDEPCGMAPPING.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |
| `INVOICETYPE_INVOICETYPE` | `COMPANYCODE`, `DIVISIONCODE`, `INVOICETYPECODE` | [`INVOICETYPE`](../SALES/INVOICETYPE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `ISDEPCGMAPPING.COMPANYCODE = INVOICETYPE.COMPANYCODE AND ISDEPCGMAPPING.DIVISIONCODE = INVOICETYPE.DIVISIONCODE AND ISDEPCGMAPPING.INVOICETYPECODE = INVOICETYPE.CODE` |
| `PORT_PORT` | `PORTCODE` | [`PORT`](../CORE_MASTER/PORT.md) | `CODE` | RESTRICT | `ISDEPCGMAPPING.PORTCODE = PORT.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ISDEPCGMAPPINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.INVOICETYPECODE,
       t.PORTCODE,
       t.EPCGAPPLICATIONCODE,
       t.EPCGAPPLICATIONDATE,
       t.EPCGLICENSENO,
       t.EPCGLICENSEDATE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.ISDEPCGMAPPING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
