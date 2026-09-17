# DB2ADMIN.PRICEDEFINITIONTEMPLATE

- **Module**: `SALES` (low confidence — FK neighbourhood: 2 of 2 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 38
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 63974

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DEFINITIONTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 5 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 6 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 7 | `DIVISIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `ORDERPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `FINANCIALORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 11 | `ORDERCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `AREAREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `STATISTICALGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 15 | `PAYMENTMETHODREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 16 | `AGENTREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `COLLECTIONREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 18 | `TERMSOFDELIVERYCODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 21 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 22 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  | FK | foreign_key |  |
| 23 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 24 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 25 | `ORDERITEMGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 26 | `QUALITYLEVELREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 27 | `LINEUSERVALUEREQUIRED` | CHAR(1) |  |  |  |  |
| 28 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 29 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 30 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 31 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 32 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 33 | `LOGMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 34 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 35 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 36 | `REFERENCEPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 37 | `REFERENCEPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMMENTCHOOSEKEYSHEADER_COMMENTCHOOSEKEYS` | `COMPANYCODE`, `ORDERTYPE`, `COMMENTCHOOSEKEYSTYPE`, `COMMENTCHOOSEKEYSCODE` | [`COMMENTCHOOSEKEYSHEADER`](../CORE_MASTER/COMMENTCHOOSEKEYSHEADER.md) | `COMPANYCODE`, `ORDERTYPE`, `TYPE`, `CODE` | RESTRICT | `PRICEDEFINITIONTEMPLATE.COMPANYCODE = COMMENTCHOOSEKEYSHEADER.COMPANYCODE AND PRICEDEFINITIONTEMPLATE.ORDERTYPE = COMMENTCHOOSEKEYSHEADER.ORDERTYPE AND PRICEDEFINITIONTEMPLATE.COMMENTCHOOSEKEYSTYPE = COMMENTCHOOSEKEYSHEADER.TYPE AND PRICEDEFINITIONTEMPLATE.COMMENTCHOOSEKEYSCODE = COMMENTCHOOSEKEYSHEADER.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PRICEDEFINITIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRICEDEFINITIONTEMPLATE_TEMPLATE` | [`SALESPRICEDEFINITION`](../SALES/SALESPRICEDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TEMPLATEDEFINITIONTYPE`, `TEMPLATECODE` | `SALESPRICEDEFINITION.COMPANYCODE = PRICEDEFINITIONTEMPLATE.COMPANYCODE AND SALESPRICEDEFINITION.ORDERTYPE = PRICEDEFINITIONTEMPLATE.ORDERTYPE AND SALESPRICEDEFINITION.TEMPLATEDEFINITIONTYPE = PRICEDEFINITIONTEMPLATE.DEFINITIONTYPE AND SALESPRICEDEFINITION.TEMPLATECODE = PRICEDEFINITIONTEMPLATE.CODE` |
| `PRICEDEFINITIONTEMPLATE_TEMPLATE` | [`SALESPRICELISTDEFINITION`](../SALES/SALESPRICELISTDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `TEMPLATEDEFINITIONTYPE`, `TEMPLATECODE` | `SALESPRICELISTDEFINITION.COMPANYCODE = PRICEDEFINITIONTEMPLATE.COMPANYCODE AND SALESPRICELISTDEFINITION.ORDERTYPE = PRICEDEFINITIONTEMPLATE.ORDERTYPE AND SALESPRICELISTDEFINITION.TEMPLATEDEFINITIONTYPE = PRICEDEFINITIONTEMPLATE.DEFINITIONTYPE AND SALESPRICELISTDEFINITION.TEMPLATECODE = PRICEDEFINITIONTEMPLATE.CODE` |

## Indexes

- `PRICEDEFINITIONTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.DEFINITIONTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.DIVISIONREQUIRED,
       t.ORDERPARTNERREQUIRED,
       t.ORDERPARTNERGROUPREQUIRED,
       t.FINANCIALORDERPARTNERREQUIRED,
       t.ORDERCATEGORYREQUIRED
FROM   DB2ADMIN.PRICEDEFINITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
