# DB2ADMIN.SALESCLAIMTEMPLATE

- **Module**: `SALES` (high confidence — table name starts with 'SALES')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 39123

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `ORDERTYPE` | CHAR(1) | NOT NULL | FK | foreign_key |  |
| 4 | `CODE` | CHAR(3) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 5 | `DOCUMENTTYPE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `RETURNREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CREDITNOTEREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CHECKPOLICYCODE` | CHAR(20) |  |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 17 | `ENTRYTRNTEMPLATECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 18 | `ENTRYTRANSACTIONTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `ENTRYCSMWAREHOUSECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ENTRYCUSTOMERWAREHOUSECODE` | CHAR(8) |  | FK | foreign_key |  |
| 21 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  | FK | foreign_key |  |
| 22 | `ENTEREDQTYGREATERCLAIMLINE` | SMALLINT | NOT NULL |  |  |  |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SALESCLAIMTEMPLATE.COMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESCLAIMTEMPLATE.COMPANYCODE = DIVISION.COMPANYCODE AND SALESCLAIMTEMPLATE.DIVISIONCODE = DIVISION.CODE` |
| `DOCUMENTTYPE_DOCUMENT` | `ORDERTYPE`, `DOCUMENTTYPE` | [`DOCUMENTTYPE`](../CORE_MASTER/DOCUMENTTYPE.md) | `ORDERTYPE`, `TYPE` | RESTRICT | `SALESCLAIMTEMPLATE.ORDERTYPE = DOCUMENTTYPE.ORDERTYPE AND SALESCLAIMTEMPLATE.DOCUMENTTYPE = DOCUMENTTYPE.TYPE` |
| `LOGICALWAREHOUSE_ENTRYCUSTOMERWAREHOUSE` | `ENTRYCSMWAREHOUSECOMPANYCODE`, `ENTRYCUSTOMERWAREHOUSECODE` | [`LOGICALWAREHOUSE`](../WAREHOUSE/LOGICALWAREHOUSE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESCLAIMTEMPLATE.ENTRYCSMWAREHOUSECOMPANYCODE = LOGICALWAREHOUSE.COMPANYCODE AND SALESCLAIMTEMPLATE.ENTRYCUSTOMERWAREHOUSECODE = LOGICALWAREHOUSE.CODE` |
| `SALESORDERTEMPLATE_DOCUMENTTEMPLATE` | `COMPANYCODE`, `DOCUMENTTEMPLATECODE` | [`SALESORDERTEMPLATE`](../SALES/SALESORDERTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESCLAIMTEMPLATE.COMPANYCODE = SALESORDERTEMPLATE.COMPANYCODE AND SALESCLAIMTEMPLATE.DOCUMENTTEMPLATECODE = SALESORDERTEMPLATE.CODE` |
| `STOCKTRANSACTIONTEMPLATE_ENTRYTRANSACTIONTEMPLATE` | `ENTRYTRNTEMPLATECOMPANYCODE`, `ENTRYTRANSACTIONTEMPLATECODE` | [`STOCKTRANSACTIONTEMPLATE`](../INVENTORY/STOCKTRANSACTIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SALESCLAIMTEMPLATE.ENTRYTRNTEMPLATECOMPANYCODE = STOCKTRANSACTIONTEMPLATE.COMPANYCODE AND SALESCLAIMTEMPLATE.ENTRYTRANSACTIONTEMPLATECODE = STOCKTRANSACTIONTEMPLATE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `SALESCLAIMTEMPLATE_CLAIMTEMPLATE` | [`SALESCLAIMLINE`](../SALES/SALESCLAIMLINE.md) | `COMPANYCODE`, `CLAIMTEMPLATECODE` | `SALESCLAIMLINE.COMPANYCODE = SALESCLAIMTEMPLATE.COMPANYCODE AND SALESCLAIMLINE.CLAIMTEMPLATECODE = SALESCLAIMTEMPLATE.CODE` |

## Indexes

- `SALESCLAIMTEMPLATEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.ORDERTYPE,
       t.CODE,
       t.DOCUMENTTYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.RETURNREQUIRED,
       t.CREDITNOTEREQUIRED,
       t.CHECKPOLICYCODE
FROM   DB2ADMIN.SALESCLAIMTEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
