# DB2ADMIN.PURCHASEPRICELISTTEMPLATE

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `COMPANYCODE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 2 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 39695

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DEFINITIONTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `ORDERCATEGORYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 7 | `STATISTICALGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 8 | `ORDERTEMPLATECODEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 9 | `PAYMENTMETHODREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 10 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `QUALITYLEVELREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 12 | `TERMSOFDELIVERYREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 13 | `COMMENTHEADERCRITERIA` | CHAR(1) | NOT NULL |  |  |  |
| 14 | `HEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 15 | `COMMENTCHOOSEKEYSORDERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 16 | `COMMENTCHOOSEKEYSTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 17 | `COMMENTCHOOSEKEYSCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 19 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 20 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 21 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 23 | `LOGMANAGEMENT` | CHAR(90) |  |  |  |  |
| 24 | `LINEUSERVALUEREQUIRED` | CHAR(1) |  |  |  |  |
| 25 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 26 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMMENTCHOOSEKEYSHEADER_COMMENTCHOOSEKEYS` | `COMPANYCODE`, `COMMENTCHOOSEKEYSORDERTYPE`, `COMMENTCHOOSEKEYSTYPE`, `COMMENTCHOOSEKEYSCODE` | [`COMMENTCHOOSEKEYSHEADER`](../CORE_MASTER/COMMENTCHOOSEKEYSHEADER.md) | `COMPANYCODE`, `ORDERTYPE`, `TYPE`, `CODE` | RESTRICT | `PURCHASEPRICELISTTEMPLATE.COMPANYCODE = COMMENTCHOOSEKEYSHEADER.COMPANYCODE AND PURCHASEPRICELISTTEMPLATE.COMMENTCHOOSEKEYSORDERTYPE = COMMENTCHOOSEKEYSHEADER.ORDERTYPE AND PURCHASEPRICELISTTEMPLATE.COMMENTCHOOSEKEYSTYPE = COMMENTCHOOSEKEYSHEADER.TYPE AND PURCHASEPRICELISTTEMPLATE.COMMENTCHOOSEKEYSCODE = COMMENTCHOOSEKEYSHEADER.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PURCHASEPRICELISTTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PURCHASEPRICELISTTEMPLATE_TEMPLATE` | [`PURCHASEPRICELINE`](../PURCHASING/PURCHASEPRICELINE.md) | `PURCHASEPRICELISTCOMPANYCODE`, `TEMPLATEDEFINITIONTYPE`, `TEMPLATECODE` | `PURCHASEPRICELINE.PURCHASEPRICELISTCOMPANYCODE = PURCHASEPRICELISTTEMPLATE.COMPANYCODE AND PURCHASEPRICELINE.TEMPLATEDEFINITIONTYPE = PURCHASEPRICELISTTEMPLATE.DEFINITIONTYPE AND PURCHASEPRICELINE.TEMPLATECODE = PURCHASEPRICELISTTEMPLATE.CODE` |
| `PURCHASEPRICELISTTEMPLATE_TEMPLATE` | [`PURCHASEPRICELIST`](../PURCHASING/PURCHASEPRICELIST.md) | `COMPANYCODE`, `TEMPLATEDEFINITIONTYPE`, `TEMPLATECODE` | `PURCHASEPRICELIST.COMPANYCODE = PURCHASEPRICELISTTEMPLATE.COMPANYCODE AND PURCHASEPRICELIST.TEMPLATEDEFINITIONTYPE = PURCHASEPRICELISTTEMPLATE.DEFINITIONTYPE AND PURCHASEPRICELIST.TEMPLATECODE = PURCHASEPRICELISTTEMPLATE.CODE` |

## Indexes

- `PURCHASEPRICELISTTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DEFINITIONTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.ORDERCATEGORYREQUIRED,
       t.STATISTICALGROUPREQUIRED,
       t.ORDERTEMPLATECODEREQUIRED,
       t.PAYMENTMETHODREQUIRED,
       t.ORDERITEMREQUIRED,
       t.QUALITYLEVELREQUIRED
FROM   DB2ADMIN.PURCHASEPRICELISTTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
