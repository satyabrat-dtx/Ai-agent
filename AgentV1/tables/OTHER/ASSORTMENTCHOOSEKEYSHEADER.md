# DB2ADMIN.ASSORTMENTCHOOSEKEYSHEADER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `CODE`
- **FK degree**: referenced by 4 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 16530

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ASSORTMENTCHOOSEKEYSHEADER.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 4

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ASSORTMENTCHOOSEKEYSHEADER_ASSORTMENTCHOOSEKEYS` | [`ASSORTMENTCHOOSEKEYS`](../OTHER/ASSORTMENTCHOOSEKEYS.md) | `ASRCHSKEYSHEADERCOMPANYCODE`, `ASRCHOOSEKEYSHEADERORDERTYPE`, `ASSORTMENTCHOOSEKEYSHEADERCODE` | `ASSORTMENTCHOOSEKEYS.ASRCHSKEYSHEADERCOMPANYCODE = ASSORTMENTCHOOSEKEYSHEADER.COMPANYCODE AND ASSORTMENTCHOOSEKEYS.ASRCHOOSEKEYSHEADERORDERTYPE = ASSORTMENTCHOOSEKEYSHEADER.ORDERTYPE AND ASSORTMENTCHOOSEKEYS.ASSORTMENTCHOOSEKEYSHEADERCODE = ASSORTMENTCHOOSEKEYSHEADER.CODE` |
| `ASSORTMENTCHOOSEKEYSHEADER_ASSORTMENTCHOOSEKEYS` | [`INTERNALORDERTEMPLATE`](../INTERNAL_ORDERS/INTERNALORDERTEMPLATE.md) | `COMPANYCODE`, `ORDERTYPE`, `ASSORTMENTCHOOSEKEYSCODE` | `INTERNALORDERTEMPLATE.COMPANYCODE = ASSORTMENTCHOOSEKEYSHEADER.COMPANYCODE AND INTERNALORDERTEMPLATE.ORDERTYPE = ASSORTMENTCHOOSEKEYSHEADER.ORDERTYPE AND INTERNALORDERTEMPLATE.ASSORTMENTCHOOSEKEYSCODE = ASSORTMENTCHOOSEKEYSHEADER.CODE` |
| `ASSORTMENTCHOOSEKEYSHEADER_ASSORTMENTCHOOSEKEYS` | [`PURCHASEORDERTEMPLATE`](../PURCHASING/PURCHASEORDERTEMPLATE.md) | `COMPANYCODE`, `ORDERTYPE`, `ASSORTMENTCHOOSEKEYSCODE` | `PURCHASEORDERTEMPLATE.COMPANYCODE = ASSORTMENTCHOOSEKEYSHEADER.COMPANYCODE AND PURCHASEORDERTEMPLATE.ORDERTYPE = ASSORTMENTCHOOSEKEYSHEADER.ORDERTYPE AND PURCHASEORDERTEMPLATE.ASSORTMENTCHOOSEKEYSCODE = ASSORTMENTCHOOSEKEYSHEADER.CODE` |
| `ASSORTMENTCHOOSEKEYSHEADER_ASSORTMENTCHOOSEKEYS` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `ORDERTYPE`, `ASSORTMENTCHOOSEKEYSCODE` | `SALESORDERTEMPLATE.COMPANYCODE = ASSORTMENTCHOOSEKEYSHEADER.COMPANYCODE AND SALESORDERTEMPLATE.ORDERTYPE = ASSORTMENTCHOOSEKEYSHEADER.ORDERTYPE AND SALESORDERTEMPLATE.ASSORTMENTCHOOSEKEYSCODE = ASSORTMENTCHOOSEKEYSHEADER.CODE` |

## Indexes

- `ASSORTMENTCHOOSEKEYSHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.ABSUNIQUEID,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.ASSORTMENTCHOOSEKEYSHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
