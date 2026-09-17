# DB2ADMIN.WRKSALESSTATISTICSREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 92
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 27701

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `EXPIRATIONDATE` | DATE |  |  |  |  |
| 3 | `COMPANY` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `CUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 5 | `CUSTOMER` | CHAR(8) |  |  |  |  |
| 6 | `LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 7 | `FNCUSTOMERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `FNCUSTOMER` | CHAR(8) |  |  |  |  |
| 9 | `FNLEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 10 | `AREA` | CHAR(3) |  |  |  |  |
| 11 | `AREADECODE` | VARCHAR(80) |  |  |  |  |
| 12 | `PROJECT` | CHAR(20) |  |  |  |  |
| 13 | `PROJECTDECODE` | VARCHAR(80) |  |  |  |  |
| 14 | `STATGROUP` | CHAR(6) |  |  |  |  |
| 15 | `STATISTICALGROUPDECODE` | VARCHAR(80) |  |  |  |  |
| 16 | `COLLECTIONGROUP` | CHAR(6) |  |  |  |  |
| 17 | `COLLECTIONGROUPDECODE` | VARCHAR(80) |  |  |  |  |
| 18 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 19 | `DOCUMENTTYPE` | CHAR(3) |  |  |  |  |
| 20 | `TEMPLATE` | CHAR(3) |  |  |  |  |
| 21 | `LINETEMPLATE` | CHAR(3) |  |  |  |  |
| 22 | `ITEMTYPE` | CHAR(3) |  |  |  |  |
| 23 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 24 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 33 | `ITEMTYPEDECODE` | VARCHAR(80) |  |  |  |  |
| 34 | `ITEMDECODE` | VARCHAR(80) |  |  |  |  |
| 35 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 36 | `INTITEMTYPE` | CHAR(3) |  |  |  |  |
| 37 | `INTSUBCODE01` | CHAR(20) |  |  |  |  |
| 38 | `INTSUBCODE02` | CHAR(10) |  |  |  |  |
| 39 | `INTSUBCODE03` | CHAR(10) |  |  |  |  |
| 40 | `INTSUBCODE04` | CHAR(10) |  |  |  |  |
| 41 | `INTSUBCODE05` | CHAR(10) |  |  |  |  |
| 42 | `INTSUBCODE06` | CHAR(10) |  |  |  |  |
| 43 | `INTSUBCODE07` | CHAR(10) |  |  |  |  |
| 44 | `INTSUBCODE08` | CHAR(10) |  |  |  |  |
| 45 | `INTSUBCODE09` | CHAR(10) |  |  |  |  |
| 46 | `INTSUBCODE10` | CHAR(10) |  |  |  |  |
| 47 | `INTITEMTYPEDECODE` | VARCHAR(80) |  |  |  |  |
| 48 | `INTITEMDECODE` | VARCHAR(80) |  |  |  |  |
| 49 | `INTITEMCODE` | VARCHAR(120) |  |  |  |  |
| 50 | `WAREHOUSE` | CHAR(8) |  |  |  |  |
| 51 | `WAREHOUSEDECODE` | VARCHAR(80) |  |  |  |  |
| 52 | `UOMPRIM` | CHAR(3) |  |  |  |  |
| 53 | `PRIMUOMDECODE` | VARCHAR(80) |  |  |  |  |
| 54 | `UOMSEC` | CHAR(3) |  |  |  |  |
| 55 | `SECUOMDECODE` | VARCHAR(80) |  |  |  |  |
| 56 | `UOMPACK` | CHAR(3) |  |  |  |  |
| 57 | `PACKUOMDECODE` | VARCHAR(80) |  |  |  |  |
| 58 | `CURRENCY` | CHAR(4) |  |  |  |  |
| 59 | `CURRENCYDECODE` | VARCHAR(80) |  |  |  |  |
| 60 | `IDOCUMENTDATE` | DATE |  |  |  |  |
| 61 | `IPROVDOCUMENTDATE` | DATE |  |  |  |  |
| 62 | `IDEFDOCUMENTDATE` | DATE |  |  |  |  |
| 63 | `QTYIPRIM` | DECIMAL(15,5) |  |  |  |  |
| 64 | `QTYISEC` | DECIMAL(15,5) |  |  |  |  |
| 65 | `QTYIPACK` | DECIMAL(15,5) |  |  |  |  |
| 66 | `INETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 67 | `ITAXINCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 68 | `IGROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 69 | `PDOCUMENTDATE` | DATE |  |  |  |  |
| 70 | `PPROVDOCUMENTDATE` | DATE |  |  |  |  |
| 71 | `PDEFDOCUMENTDATE` | DATE |  |  |  |  |
| 72 | `QTYPPRIM` | DECIMAL(15,5) |  |  |  |  |
| 73 | `QTYPSEC` | DECIMAL(15,5) |  |  |  |  |
| 74 | `QTYPPACK` | DECIMAL(15,5) |  |  |  |  |
| 75 | `PNETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 76 | `PTAXINCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 77 | `PGROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 78 | `NDOCUMENTDATE` | DATE |  |  |  |  |
| 79 | `NPROVDOCUMENTDATE` | DATE |  |  |  |  |
| 80 | `NDEFDOCUMENTDATE` | DATE |  |  |  |  |
| 81 | `QTYNPRIM` | DECIMAL(15,5) |  |  |  |  |
| 82 | `QTYNSEC` | DECIMAL(15,5) |  |  |  |  |
| 83 | `QTYNPACK` | DECIMAL(15,5) |  |  |  |  |
| 84 | `NNETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 85 | `NTAXINCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 86 | `NGROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 87 | `AGENT1` | CHAR(3) |  |  |  |  |
| 88 | `AGENT2` | CHAR(3) |  |  |  |  |
| 89 | `AGENT3` | CHAR(3) |  |  |  |  |
| 90 | `AGENT4` | CHAR(3) |  |  |  |  |
| 91 | `AGENT5` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINE,
       t.EXPIRATIONDATE,
       t.COMPANY,
       t.CUSTOMERTYPE,
       t.CUSTOMER,
       t.LEGALNAME1,
       t.FNCUSTOMERTYPE,
       t.FNCUSTOMER,
       t.FNLEGALNAME1,
       t.AREA,
       t.AREADECODE
FROM   DB2ADMIN.WRKSALESSTATISTICSREPORT t
FETCH FIRST 100 ROWS ONLY;
```
