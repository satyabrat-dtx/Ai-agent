# DB2ADMIN.TABELEMENTSERVICES

- **Module**: `COSTING` (low confidence — FK neighbourhood: 1 of 1 related tables are COSTING)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `COSTELEMENTITEMTYPECODE`, `COSTELEMENTSUBCODE01`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 97347

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COSTELEMENTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `COSTELEMENTITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `COSTELEMENTSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 4 | `SERVICECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `SERVICEITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `SERVICESUBCODE01` | CHAR(20) |  | FK | foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `TABELEMENTSERVICES.COMPANYCODE = COMPANY.CODE` |
| `SERVICES_SERVICE` | `SERVICECOMPANYCODE`, `SERVICEITEMTYPECODE`, `SERVICESUBCODE01` | [`SERVICES`](../COSTING/SERVICES.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `TABELEMENTSERVICES.SERVICECOMPANYCODE = SERVICES.COMPANYCODE AND TABELEMENTSERVICES.SERVICEITEMTYPECODE = SERVICES.ITEMTYPECODE AND TABELEMENTSERVICES.SERVICESUBCODE01 = SERVICES.SUBCODE01` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TABELEMENTSERVICESUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COSTELEMENTCOMPANYCODE,
       t.COSTELEMENTITEMTYPECODE,
       t.COSTELEMENTSUBCODE01,
       t.SERVICECOMPANYCODE,
       t.SERVICEITEMTYPECODE,
       t.SERVICESUBCODE01,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TABELEMENTSERVICES t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
