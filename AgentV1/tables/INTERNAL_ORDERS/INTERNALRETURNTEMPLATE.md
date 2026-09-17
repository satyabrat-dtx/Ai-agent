# DB2ADMIN.INTERNALRETURNTEMPLATE

- **Module**: `INTERNAL_ORDERS` (high confidence — table name starts with 'INTERNAL')
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 38755

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
| 7 | `AUTHORIZATIONCHECKPHASE` | CHAR(90) |  |  |  |  |
| 8 | `RETURNSTOCKTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 9 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `CHECKPOLICYCODE` | CHAR(20) |  |  |  |  |
| 11 | `CUSTOMIZEUIPOLICYCODE` | CHAR(20) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `LEGALDOCUMENTTYPECODE` | CHAR(4) |  | FK | foreign_key |  |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTERNALRETURNTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALRETURNTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND INTERNALRETURNTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | [`LEGALDOCUMENTTYPE`](../CORE_MASTER/LEGALDOCUMENTTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALRETURNTEMPLATE.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND INTERNALRETURNTEMPLATE.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_STOCKTRANSACTIONTEMPLATE` | `STOCKTRNTEMPLATECOMPANYCODE`, `STOCKTRANSACTIONTEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `INTERNALRETURNTEMPLATE.STOCKTRNTEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND INTERNALRETURNTEMPLATE.STOCKTRANSACTIONTEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |
| `STOCKTYPE_RETURNSTOCKTYPE` | `RETURNSTOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `INTERNALRETURNTEMPLATE.RETURNSTOCKTYPECODE = STOCKTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INTERNALRETURNTEMPLATE_TEMPLATE` | [`INTERNALRETURNDOCUMENT`](../INTERNAL_ORDERS/INTERNALRETURNDOCUMENT.md) | `COMPANYCODE`, `TEMPLATECODE` | `INTERNALRETURNDOCUMENT.COMPANYCODE = INTERNALRETURNTEMPLATE.COMPANYCODE AND INTERNALRETURNDOCUMENT.TEMPLATECODE = INTERNALRETURNTEMPLATE.CODE` |

## Indexes

- `INTERNALRETURNTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.AUTHORIZATIONCHECKPHASE,
       t.RETURNSTOCKTYPECODE,
       t.STOCKTRANSACTIONTEMPLATECODE,
       t.CHECKPOLICYCODE,
       t.CUSTOMIZEUIPOLICYCODE
FROM   DB2ADMIN.INTERNALRETURNTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
