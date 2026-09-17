# DB2ADMIN.FINGSTINVOICETAXMAP

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `POSITION`, `REPORTCODE`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 180076

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `POSITION` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COLUMNTITLE` | CHAR(50) |  |  |  |  |
| 4 | `CALCULATIONTYPE` | INTEGER | NOT NULL |  |  |  |
| 5 | `REPORTCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FINGSTINVOICETAXMAP.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `FINGSTINVOICETAXMAP_TAXDETAIL` | [`FINGSTINVOICETAXMAPDETAIL`](../FINANCE/FINGSTINVOICETAXMAPDETAIL.md) | `FINGSTINVOICETAXMAPCOMPANYCODE`, `FINGSTINVOICETAXMAPDIVISIONCOD`, `FINGSTINVOICETAXMAPPOSITION`, `FINGSTINVOICETAXMAPREPORTCODE` | `FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPCOMPANYCODE = FINGSTINVOICETAXMAP.COMPANYCODE AND FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPDIVISIONCOD = FINGSTINVOICETAXMAP.DIVISIONCODE AND FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPPOSITION = FINGSTINVOICETAXMAP.POSITION AND FINGSTINVOICETAXMAPDETAIL.FINGSTINVOICETAXMAPREPORTCODE = FINGSTINVOICETAXMAP.REPORTCODE` |
| `FINGSTINVOICETAXMAP_ALLOWEDVALUESDETAIL` | [`FINGSTREPORTALLOWEDVALUES`](../FINANCE/FINGSTREPORTALLOWEDVALUES.md) | `FINGSTINVOICETAXMAPCOMPANYCODE`, `FINGSTINVOICETAXMAPDIVISIONCOD`, `FINGSTINVOICETAXMAPPOSITION`, `FINGSTINVOICETAXMAPREPORTCODE` | `FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPCOMPANYCODE = FINGSTINVOICETAXMAP.COMPANYCODE AND FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPDIVISIONCOD = FINGSTINVOICETAXMAP.DIVISIONCODE AND FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPPOSITION = FINGSTINVOICETAXMAP.POSITION AND FINGSTREPORTALLOWEDVALUES.FINGSTINVOICETAXMAPREPORTCODE = FINGSTINVOICETAXMAP.REPORTCODE` |

## Indexes

- `FINGSTINVOICETAXMAPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.POSITION,
       t.COLUMNTITLE,
       t.CALCULATIONTYPE,
       t.REPORTCODE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.FINGSTINVOICETAXMAP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
