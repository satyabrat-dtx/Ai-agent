# DB2ADMIN.BLOCKSDEFINITIONTEMPLATE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `DEFINITIONTYPE`, `CODE`
- **FK degree**: referenced by 3 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27374

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
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
| 16 | `ITEMTYPEREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 17 | `ORDERITEMREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 18 | `ORDERITEMGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 19 | `QUALITYLEVELREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 20 | `LINEUSERVALUEREQUIRED` | CHAR(1) |  |  |  |  |
| 21 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 22 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 23 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 24 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 26 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 27 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 28 | `REFERENCEPARTNERREQUIRED` | CHAR(1) | NOT NULL |  |  |  |
| 29 | `REFERENCEPARTNERGROUPREQUIRED` | CHAR(1) | NOT NULL |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BLOCKSDEFINITIONTEMPLATE.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 3

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `BLOCKSDEFINITIONTEMPLATE_TEMPLATE` | [`SALESBLOCKSDEFINITION`](../SALES/SALESBLOCKSDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `BLOCKTYPE`, `TEMPLATECODE` | `SALESBLOCKSDEFINITION.COMPANYCODE = BLOCKSDEFINITIONTEMPLATE.COMPANYCODE AND SALESBLOCKSDEFINITION.ORDERTYPE = BLOCKSDEFINITIONTEMPLATE.ORDERTYPE AND SALESBLOCKSDEFINITION.BLOCKTYPE = BLOCKSDEFINITIONTEMPLATE.DEFINITIONTYPE AND SALESBLOCKSDEFINITION.TEMPLATECODE = BLOCKSDEFINITIONTEMPLATE.CODE` |
| `BLOCKSDEFINITIONTEMPLATE_TEMPLATE` | [`INTERNALBLOCKSDEFINITION`](../INTERNAL_ORDERS/INTERNALBLOCKSDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `BLOCKTYPE`, `TEMPLATECODE` | `INTERNALBLOCKSDEFINITION.COMPANYCODE = BLOCKSDEFINITIONTEMPLATE.COMPANYCODE AND INTERNALBLOCKSDEFINITION.ORDERTYPE = BLOCKSDEFINITIONTEMPLATE.ORDERTYPE AND INTERNALBLOCKSDEFINITION.BLOCKTYPE = BLOCKSDEFINITIONTEMPLATE.DEFINITIONTYPE AND INTERNALBLOCKSDEFINITION.TEMPLATECODE = BLOCKSDEFINITIONTEMPLATE.CODE` |
| `BLOCKSDEFINITIONTEMPLATE_TEMPLATE` | [`PURCHASEBLOCKSDEFINITION`](../PURCHASING/PURCHASEBLOCKSDEFINITION.md) | `COMPANYCODE`, `ORDERTYPE`, `BLOCKTYPE`, `TEMPLATECODE` | `PURCHASEBLOCKSDEFINITION.COMPANYCODE = BLOCKSDEFINITIONTEMPLATE.COMPANYCODE AND PURCHASEBLOCKSDEFINITION.ORDERTYPE = BLOCKSDEFINITIONTEMPLATE.ORDERTYPE AND PURCHASEBLOCKSDEFINITION.BLOCKTYPE = BLOCKSDEFINITIONTEMPLATE.DEFINITIONTYPE AND PURCHASEBLOCKSDEFINITION.TEMPLATECODE = BLOCKSDEFINITIONTEMPLATE.CODE` |

## Indexes

- `BLOCKSDEFINITIONTEMPLATEUID` (ABSUNIQUEID)

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
FROM   DB2ADMIN.BLOCKSDEFINITIONTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
