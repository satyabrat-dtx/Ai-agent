# DB2ADMIN.ASSORTMENTDEFINITIONTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 9290

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `DIVISIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `FINANCIALORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ORDERCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `AREAREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `STATISTICALGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `AGENTREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `REFERENCEPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 23 | `REFERENCEPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ASSORTMENTDEFINITIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ASSORTMENTDEFINITIONTEMPLATE_TEMPLATE` | [`INTERNALASSORTMENTDEFINITION`](../INTERNAL_ORDERS/INTERNALASSORTMENTDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TEMPLATECODE` | `INTERNALASSORTMENTDEFINITION.COMPANYCODE = ASSORTMENTDEFINITIONTEMPLATE.COMPANYCODE AND INTERNALASSORTMENTDEFINITION.ORDERTYPE = ASSORTMENTDEFINITIONTEMPLATE.ORDERTYPE AND INTERNALASSORTMENTDEFINITION.TEMPLATECODE = ASSORTMENTDEFINITIONTEMPLATE.CODE` |
| `ASSORTMENTDEFINITIONTEMPLATE_TEMPLATE` | [`PURCHASEASSORTMENTDEFINITION`](../PURCHASING/PURCHASEASSORTMENTDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TEMPLATECODE` | `PURCHASEASSORTMENTDEFINITION.COMPANYCODE = ASSORTMENTDEFINITIONTEMPLATE.COMPANYCODE AND PURCHASEASSORTMENTDEFINITION.ORDERTYPE = ASSORTMENTDEFINITIONTEMPLATE.ORDERTYPE AND PURCHASEASSORTMENTDEFINITION.TEMPLATECODE = ASSORTMENTDEFINITIONTEMPLATE.CODE` |
| `ASSORTMENTDEFINITIONTEMPLATE_TEMPLATE` | [`SALESASSORTMENTDEFINITION`](../SALES/SALESASSORTMENTDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TEMPLATECODE` | `SALESASSORTMENTDEFINITION.COMPANYCODE = ASSORTMENTDEFINITIONTEMPLATE.COMPANYCODE AND SALESASSORTMENTDEFINITION.ORDERTYPE = ASSORTMENTDEFINITIONTEMPLATE.ORDERTYPE AND SALESASSORTMENTDEFINITION.TEMPLATECODE = ASSORTMENTDEFINITIONTEMPLATE.CODE` |

## Indexes

- `ASRDEFINITIONTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DIVISIONREQUIRED,
       t.ORDERPARTNERREQUIRED,
       t.ORDERPARTNERGROUPREQUIRED,
       t.FINANCIALORDERPARTNERREQUIRED,
       t.ORDERCATEGORYREQUIRED,
       t.AREAREQUIRED
FROM   DB2ADMIN.ASSORTMENTDEFINITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
