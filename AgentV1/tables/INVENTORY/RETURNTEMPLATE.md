# DB2ADMIN.RETURNTEMPLATE

- **Module**: `INVENTORY` (low confidence — FK neighbourhood: 2 of 3 related tables are INVENTORY)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 8 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 39066

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
| 18 | `RETURNCOUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `RETURNCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 20 | `RETURNDEFINITIVECNTCMYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `RETURNDEFINITIVECOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 22 | `TERMSOFLOGORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 23 | `TERMSOFLOGCODE` | CHAR(2) |  | FK | foreign_key |  |
| 24 | `LEGALDOCUMENTTYPECODE` | CHAR(4) |  | FK | foreign_key |  |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 8

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `RETURNTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `COUNTER_RETURNCOUNTER` | `RETURNCOUNTERCOMPANYCODE`, `RETURNCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RETURNTEMPLATE.RETURNCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND RETURNTEMPLATE.RETURNCOUNTERCODE = COUNTER.CODE` |
| `COUNTER_RETURNDEFINITIVECOUNTER` | `RETURNDEFINITIVECNTCMYCODE`, `RETURNDEFINITIVECOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RETURNTEMPLATE.RETURNDEFINITIVECNTCMYCODE = COUNTER.COMPANYCODE AND RETURNTEMPLATE.RETURNDEFINITIVECOUNTERCODE = COUNTER.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RETURNTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND RETURNTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `LEGALDOCUMENTTYPE_LEGALDOCUMENTTYPE` | `COMPANYCODE`, `LEGALDOCUMENTTYPECODE` | [`LEGALDOCUMENTTYPE`](../CORE_MASTER/LEGALDOCUMENTTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RETURNTEMPLATE.COMPANYCODE = LEGALDOCUMENTTYPE.COMPANYCODE AND RETURNTEMPLATE.LEGALDOCUMENTTYPECODE = LEGALDOCUMENTTYPE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_STOCKTRANSACTIONTEMPLATE` | `STOCKTRNTEMPLATECOMPANYCODE`, `STOCKTRANSACTIONTEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `RETURNTEMPLATE.STOCKTRNTEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND RETURNTEMPLATE.STOCKTRANSACTIONTEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |
| `STOCKTYPE_RETURNSTOCKTYPE` | `RETURNSTOCKTYPECODE` | [`STOCKTYPE`](../INVENTORY/STOCKTYPE.md) | `CODE` | RESTRICT | `RETURNTEMPLATE.RETURNSTOCKTYPECODE = STOCKTYPE.CODE` |
| `TERMSOFLOG_TERMSOFLOG` | `COMPANYCODE`, `TERMSOFLOGORDERTYPE`, `TERMSOFLOGCODE` | [`TERMSOFLOG`](../CORE_MASTER/TERMSOFLOG.md) | `COMPANYCODE`, `ORDERTYPE`, `CODE` | RESTRICT | `RETURNTEMPLATE.COMPANYCODE = TERMSOFLOG.COMPANYCODE AND RETURNTEMPLATE.TERMSOFLOGORDERTYPE = TERMSOFLOG.ORDERTYPE AND RETURNTEMPLATE.TERMSOFLOGCODE = TERMSOFLOG.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `RETURNTEMPLATE_TEMPLATE` | [`PURCHASERETURNDOCUMENT`](../PURCHASING/PURCHASERETURNDOCUMENT.md) | `COMPANYCODE`, `TEMPLATECODE` | `PURCHASERETURNDOCUMENT.COMPANYCODE = RETURNTEMPLATE.COMPANYCODE AND PURCHASERETURNDOCUMENT.TEMPLATECODE = RETURNTEMPLATE.CODE` |

## Indexes

- `RETURNTEMPLATEUID` (ABSUNIQUEID)

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
FROM   DB2ADMIN.RETURNTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
