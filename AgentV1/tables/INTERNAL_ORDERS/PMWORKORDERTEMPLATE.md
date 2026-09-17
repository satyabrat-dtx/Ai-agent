# DB2ADMIN.PMWORKORDERTEMPLATE

- **Module**: `INTERNAL_ORDERS` (low confidence — FK neighbourhood: 2 of 3 related tables are INTERNAL_ORDERS)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 108849

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `REQUISITIONTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `INTERNALDOCUMENTTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `INTDOCUMENTLINETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `SPARESISSUETEMPLATECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `SPARESISSUETEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `AUTOCLOSELINES` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PMWORKORDERTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMWORKORDERTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND PMWORKORDERTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `INTERNALORDERLINETEMPLATE_INTERNALDOCUMENTLINETEMPLATE` | `COMPANYCODE`, `INTDOCUMENTLINETEMPLATECODE` | [`INTERNALORDERLINETEMPLATE`](../INTERNAL_ORDERS/INTERNALORDERLINETEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMWORKORDERTEMPLATE.COMPANYCODE = INTERNALORDERLINETEMPLATE.COMPANYCODE AND PMWORKORDERTEMPLATE.INTDOCUMENTLINETEMPLATECODE = INTERNALORDERLINETEMPLATE.CODE` |
| `INTERNALORDERTEMPLATE_INTERNALDOCUMENTTEMPLATE` | `COMPANYCODE`, `INTERNALDOCUMENTTEMPLATECODE` | [`INTERNALORDERTEMPLATE`](../INTERNAL_ORDERS/INTERNALORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMWORKORDERTEMPLATE.COMPANYCODE = INTERNALORDERTEMPLATE.COMPANYCODE AND PMWORKORDERTEMPLATE.INTERNALDOCUMENTTEMPLATECODE = INTERNALORDERTEMPLATE.CODE` |
| `REQUISITIONTEMPLATE_REQUISITIONTEMPLATE` | `COMPANYCODE`, `REQUISITIONTEMPLATECODE` | [`REQUISITIONTEMPLATE`](../CORE_MASTER/REQUISITIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMWORKORDERTEMPLATE.COMPANYCODE = REQUISITIONTEMPLATE.COMPANYCODE AND PMWORKORDERTEMPLATE.REQUISITIONTEMPLATECODE = REQUISITIONTEMPLATE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_SPARESISSUETEMPLATE` | `SPARESISSUETEMPLATECOMPANYCODE`, `SPARESISSUETEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PMWORKORDERTEMPLATE.SPARESISSUETEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND PMWORKORDERTEMPLATE.SPARESISSUETEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PMWORKORDERTEMPLATE_TEMPLATE` | [`PMWORKORDER`](../INTERNAL_ORDERS/PMWORKORDER.md) | `COMPANYCODE`, `TEMPLATECODE` | `PMWORKORDER.COMPANYCODE = PMWORKORDERTEMPLATE.COMPANYCODE AND PMWORKORDER.TEMPLATECODE = PMWORKORDERTEMPLATE.CODE` |

## Indexes

- `PMWORKORDERTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.REQUISITIONTEMPLATECODE,
       t.INTERNALDOCUMENTTEMPLATECODE,
       t.INTDOCUMENTLINETEMPLATECODE,
       t.SPARESISSUETEMPLATECOMPANYCODE,
       t.SPARESISSUETEMPLATECODE
FROM   DB2ADMIN.PMWORKORDERTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
