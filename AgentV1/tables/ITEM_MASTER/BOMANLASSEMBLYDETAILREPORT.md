# DB2ADMIN.BOMANLASSEMBLYDETAILREPORT

- **Module**: `ITEM_MASTER` (high confidence — table name starts with 'BOM')
- **Roles**: `business_data`
- **Columns**: 50
- **Primary key**: `IDENTIFIER`, `PROGRESSIVE`, `SUBPROGRESSIVE`
- **FK degree**: referenced by 0 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 20019

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IDENTIFIER` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `PROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `SUBPROGRESSIVE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  | FK | foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `LONGDESCRIPTION` | VARCHAR(200) | NOT NULL |  | description | Long human-readable label. |
| 16 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 17 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 18 | `BASEPRIMARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 19 | `BASESECONDARYUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `SECONDARYUNSTEADYCVSFACTOR` | DECIMAL(11,5) |  |  |  |  |
| 21 | `CONVERSIONFACTORTYPE` | CHAR(2) |  |  |  |  |
| 22 | `MULTIPLIER` | DECIMAL(11,5) |  |  |  |  |
| 23 | `CONVERSIONFACTORPOLICYCODE` | CHAR(20) |  |  |  |  |
| 24 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 25 | `PRODUCTIONUOMTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 26 | `PRODUCTIONUNITCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `STDPRODUCTIONBATCH` | DECIMAL(15,5) |  |  |  |  |
| 28 | `BOMITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 29 | `BOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 30 | `BOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 31 | `BOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 32 | `BOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 33 | `BOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 34 | `BOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 35 | `BOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 36 | `BOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 37 | `BOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 38 | `BOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 39 | `STATUS` | CHAR(1) | NOT NULL |  |  |  |
| 40 | `APPROVALDATE` | DATE |  |  |  |  |
| 41 | `APPROVALUSER` | CHAR(50) |  |  |  |  |
| 42 | `RELEASEDATE` | DATE |  |  |  |  |
| 43 | `RELEASEUSER` | CHAR(50) |  |  |  |  |
| 44 | `VALIDITYSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 45 | `INITIALDATE` | DATE |  |  |  |  |
| 46 | `FINALDATE` | DATE |  |  |  |  |
| 47 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 48 | `BOMITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 49 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BOMANLASSEMBLYDETAILREPORT.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_BOMITEMTYPE` | `BOMITEMTYPECOMPANYCODE`, `BOMITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMANLASSEMBLYDETAILREPORT.BOMITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND BOMANLASSEMBLYDETAILREPORT.BOMITEMTYPECODE = ITEMTYPE.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BOMANLASSEMBLYDETAILREPORT.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND BOMANLASSEMBLYDETAILREPORT.ITEMTYPECODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_BASEPRIMARYUNIT` | `BASEPRIMARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BOMANLASSEMBLYDETAILREPORT.BASEPRIMARYUNITCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_BASESECONDARYUNIT` | `BASESECONDARYUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BOMANLASSEMBLYDETAILREPORT.BASESECONDARYUNITCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_PRODUCTIONUNIT` | `PRODUCTIONUNITCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `BOMANLASSEMBLYDETAILREPORT.PRODUCTIONUNITCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BOMANLASSEMBLYDLTREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IDENTIFIER,
       t.PROGRESSIVE,
       t.SUBPROGRESSIVE,
       t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.BOMANLASSEMBLYDETAILREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
