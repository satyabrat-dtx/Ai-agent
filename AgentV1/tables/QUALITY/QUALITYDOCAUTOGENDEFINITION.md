# DB2ADMIN.QUALITYDOCAUTOGENDEFINITION

- **Module**: `QUALITY` (high confidence — table name starts with 'QUALITY')
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `COMPANYCODE`, `OPERATIONTYPE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `QAITEMGROUPCODE`, `WORKCENTERCODE`, `OPERATIONCODE`, `DEMANDTEMPLATECODE`, `PROGRESSTEMPLATECODE`, `STOCKTRANSACTIONTEMPLATECODE`, `LOGICALWAREHOUSECODE`, `ORDERPARTNERREQUIRED`, `ORDPRNCUSTOMERSUPPLIERCODE`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 112587

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `OPERATIONTYPE` | CHAR(2) | NOT NULL | PK | primary_key |  |
| 2 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 3 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `QAITEMGROUPCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 15 | `WORKCENTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 16 | `OPERATIONCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 17 | `DEMANDTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 18 | `PROGRESSTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `STOCKTRNTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 20 | `STOCKTRANSACTIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 21 | `LOGICALWAREHOUSECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 22 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 23 | `ORDERPARTNERREQUIRED` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 24 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 25 | `SEQUENCE` | INTEGER | NOT NULL |  |  |  |
| 26 | `DETAILREQUIRED` | CHAR(2) | NOT NULL |  |  |  |
| 27 | `HEADERCODE` | CHAR(20) |  |  |  |  |
| 28 | `HEADERSUBGROUPCODE` | CHAR(5) |  |  |  |  |
| 29 | `HEADERNUMBERID` | INTEGER | NOT NULL |  |  |  |
| 30 | `WORKINGCALENDARCODE` | CHAR(3) |  | FK | foreign_key |  |
| 31 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 32 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 33 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 34 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 35 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 36 | `QAITEMGROUPCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 37 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 38 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 39 | `PROGRESSTEMPLATECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 40 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 41 | `DEFINITIONCHECKCODE` | CHAR(20) |  |  |  |  |
| 42 | `OCCURRENCESCHECK` | SMALLINT | NOT NULL |  |  |  |
| 43 | `OVERRIDEFREQUENCYINFO` | SMALLINT | NOT NULL |  |  |  |
| 44 | `FREQUENCYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 45 | `FREQUENCY` | INTEGER | NOT NULL |  |  |  |
| 46 | `QUANTITYCHECK` | SMALLINT | NOT NULL |  |  |  |
| 47 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 48 | `OCCURRENCES` | INTEGER | NOT NULL |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `QUALITYDOCAUTOGENDEFINITION.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `QUALITYDOCAUTOGENDEFINITION.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND QUALITYDOCAUTOGENDEFINITION.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `WORKINGCALENDAR_WORKINGCALENDAR` | `WORKINGCALENDARCODE` | [`WORKINGCALENDAR`](../CORE_MASTER/WORKINGCALENDAR.md) | `CODE` | RESTRICT | `QUALITYDOCAUTOGENDEFINITION.WORKINGCALENDARCODE = WORKINGCALENDAR.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `QUALITYDOCAUTOGENDEFUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.OPERATIONTYPE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.QUALITYDOCAUTOGENDEFINITION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
